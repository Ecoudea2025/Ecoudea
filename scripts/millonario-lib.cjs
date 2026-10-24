/**
 * millonario-lib.cjs — Validaciones compartidas del banco de preguntas
 * "¿Quién quiere ser millonario?" de Ecoudea.
 * Consumido por scripts/build-millonario.cjs y scripts/check-millonario.cjs.
 */
'use strict';

const BANNED_OPTION =/(?:todas\s+(?:las\s+)?anteriores|ninguna\s+(?:de\s+)?(?:las\s+)?anteriores)/i;

/**
 * Verifica que los delimitadores de LaTeX `$` estén balanceados.
 * Se eliminan primero los bloques display `$$`; el resto debe tener un
 * número par de `$` individuales.
 */
function latexBalanced(text) {
  if (typeof text !== 'string') return false;
  const noDisplay = text.replace(/\$\$/g, '');
  const count = (noDisplay.match(/\$/g) || []).length;
  return count % 2 === 0;
}

function normalize(text) {
  return String(text).trim().toLowerCase().replace(/\s+/g, ' ');
}

function countPerLevel(questions) {
  const per = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
  for (const q of questions) per[q.difficulty] = (per[q.difficulty] || 0) + 1;
  return per;
}

/**
 * Distribución de n niveles en 5 dificultades (igual que el motor):
 * buckets casi iguales; el sobrante (n % 5) va a las primeras dificultades.
 */
function levelSizes(total) {
  const base = Math.floor(total / 5);
  const rem = total - base * 5;
  const sizes = [];
  for (let i = 0; i < 5; i++) sizes.push(i < rem ? base + 1 : base);
  return sizes;
}

/** Redondeo "bonito" para la escalera de premios (50/500/5.000/50.000). */
function niceRound(v) {
  if (v >= 100000) return Math.round(v / 50000) * 50000;
  if (v >= 10000) return Math.round(v / 5000) * 5000;
  if (v >= 1000) return Math.round(v / 500) * 500;
  return Math.max(50, Math.round(v / 50) * 50);
}

/**
 * Valida el banco consolidado. Devuelve un array de mensajes de error
 * (vacío si el banco es válido).
 * opcional `knownSources`: Set con los nombres de clase que existen en
 * src/content/classes/ para verificar el campo `source`.
 */
function validate(bank, { knownSources = null } = {}) {
  const errors = [];

  const push = (msg) => errors.push(msg);

  // --- Estructura raíz -------------------------------------------------
  if (typeof bank !== 'object' || bank === null || Array.isArray(bank)) {
    push('El banco debe ser un objeto con "meta", "config" y "questions".');
    return errors;
  }
  if (typeof bank.meta !== 'object' || bank.meta === null) {
    push('meta: falta el bloque "meta".');
  }
  if (typeof bank.config !== 'object' || bank.config === null) {
    push('config: falta el bloque "config".');
  }
  if (!Array.isArray(bank.questions)) {
    push('questions: debe ser un array de preguntas.');
    return errors;
  }

  // --- Config (parametrizada: la partida dura = a las preguntas del banco) ---
  if (bank.config) {
    const { questionsPerGame, timePerQuestion, prizes, safeHavens } = bank.config;
    if (!Number.isInteger(questionsPerGame) || questionsPerGame < 5 || questionsPerGame > 50) {
      push(`config.questionsPerGame inválido: ${JSON.stringify(questionsPerGame)}`);
    }
    if (!Number.isInteger(timePerQuestion) || timePerQuestion < 5 || timePerQuestion > 300) {
      push(`config.timePerQuestion inválido: ${JSON.stringify(timePerQuestion)}`);
    }
    if (!Array.isArray(prizes) || prizes.length !== questionsPerGame) {
      push(`config.prizes debe tener ${questionsPerGame} premios (tiene ${Array.isArray(prizes) ? prizes.length : 'no-array'}).`);
    } else if (prizes.some((p) => !Number.isInteger(p) || p <= 0)) {
      push('config.prizes debe contener enteros positivos.');
    }
    const n = Number.isInteger(questionsPerGame) ? questionsPerGame : 15;
    if (!Array.isArray(safeHavens) || safeHavens.length !== 2) {
      push('config.safeHavens debe ser un array de 2 niveles (índices 1-based).');
    } else if (safeHavens.some((s) => !Number.isInteger(s) || s < 1 || s > n)) {
      push(`config.safeHavens fuera de rango 1..${n}: ${JSON.stringify(safeHavens)}`);
    }
  }

  // --- Preguntas --------------------------------------------------------
  const seenIds = new Set();
  const seenQuestions = new Map();
  const perLevel = countPerLevel(bank.questions);

  bank.questions.forEach((q, i) => {
    const label = `questions[${i}]${q && q.id ? ` (${q.id})` : ''}`;

    if (typeof q !== 'object' || q === null) {
      push(`${label}: no es un objeto.`);
      return;
    }

    // id (con prefijo de banco: course-001 o mq-001 del fixture de tests)
    if (typeof q.id !== 'string' || !/^[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*-\d{3}$/.test(q.id)) {
      push(`${label}: id inválido (se espera "prefijo-NNN"), recibido: ${JSON.stringify(q.id)}`);
    } else {
      if (seenIds.has(q.id)) push(`${label}: id duplicado ${q.id}.`);
      seenIds.add(q.id);
    }

    // difficulty
    if (!Number.isInteger(q.difficulty) || q.difficulty < 1 || q.difficulty > 5) {
      push(`${label}: dificultad debe ser un entero 1..5, recibida: ${JSON.stringify(q.difficulty)}.`);
    }

    // category / source
    if (typeof q.category !== 'string' || q.category.trim().length === 0) {
      push(`${label}: falta "category".`);
    }
    if (typeof q.source !== 'string' || q.source.trim().length === 0) {
      push(`${label}: falta "source" (clase que justifica la pregunta).`);
    } else if (knownSources && !knownSources.has(q.source)) {
      push(`${label}: source "${q.source}" no existe en src/content/classes/.`);
    }

    // question
    if (typeof q.question !== 'string') {
      push(`${label}: falta el texto de la pregunta.`);
    } else {
      if (q.question.trim().length < 10) push(`${label}: pregunta demasiado corta.`);
      if (q.question.length > 400) push(`${label}: pregunta demasiado larga (>400 caracteres).`);
      if (/\n/.test(q.question)) push(`${label}: la pregunta no debe contener saltos de línea.`);
      if (!latexBalanced(q.question)) push(`${label}: LaTeX desbalanceado en "question" ($ impares).`);
    }

    // options
    if (!Array.isArray(q.options) || q.options.length !== 4) {
      push(`${label}: "options" debe ser un array de exactamente 4 cadenas.`);
    } else {
      const seen = new Map();
      q.options.forEach((opt, j) => {
        if (typeof opt !== 'string' || opt.trim().length === 0) {
          push(`${label}: opción ${j + 1} vacía o no es texto.`);
          return;
        }
        if (opt.trim().length < 2) push(`${label}: opción ${j + 1} demasiado corta (mínimo 2 caracteres).`);
        if (opt.length > 220) push(`${label}: opción ${j + 1} demasiado larga (>220 caracteres).`);
        if (/\n/.test(opt)) push(`${label}: la opción ${j + 1} no debe contener saltos de línea.`);
        if (BANNED_OPTION.test(opt)) push(`${label}: la opción ${j + 1} usa "todas/ninguna de las anteriores" (prohibido).`);
        if (!latexBalanced(opt)) push(`${label}: LaTeX desbalanceado en opción ${j + 1}.`);
        const key = normalize(opt);
        if (seen.has(key)) push(`${label}: las opciones ${seen.get(key)} y ${j + 1} están duplicadas.`);
        seen.set(key, j + 1);
      });
    }

    // correct
    if (!Number.isInteger(q.correct) || q.correct < 0 || q.correct > 3) {
      push(`${label}: "correct" debe ser el índice 0..3 de la opción correcta, recibido: ${JSON.stringify(q.correct)}.`);
    }

    // explanation
    if (typeof q.explanation !== 'string' || q.explanation.trim().length < 10) {
      push(`${label}: falta "explanation" o es demasiado corta.`);
    } else if (!latexBalanced(q.explanation)) {
      push(`${label}: LaTeX desbalanceado en "explanation".`);
    }

    // duplicados exactos de enunciado
    if (typeof q.question === 'string') {
      const key = normalize(q.question);
      if (seenQuestions.has(key)) {
        push(`${label}: enunciado duplicado con ${seenQuestions.get(key)}.`);
      } else {
        seenQuestions.set(key, q.id || i);
      }
    }
  });

  // --- Cobertura por dificultad (parametrizada: bucket sizes por N) --------
  const total = bank.config && Number.isInteger(bank.config.questionsPerGame)
    ? bank.config.questionsPerGame
    : bank.questions.length;
  const sizes = levelSizes(total);
  for (let level = 1; level <= 5; level++) {
    const need = sizes[level - 1];
    if (perLevel[level] < need) {
      push(`Dificultad ${level}: tiene ${perLevel[level]} pregunta(s); la partida de ${total} niveles necesita ${need}.`);
    }
  }

  // --- meta coherente ------------------------------------------------------
  if (bank.meta) {
    if (bank.meta.questionCount !== bank.questions.length) {
      push(`meta.questionCount (${bank.meta.questionCount}) no coincide con el total (${bank.questions.length}).`);
    }
    if (bank.meta.perLevel && JSON.stringify(bank.meta.perLevel) !== JSON.stringify(perLevel)) {
      push('meta.perLevel no coincide con la distribución real del banco.');
    }
    if (bank.meta.updated && !/^\d{4}-\d{2}-\d{2}$/.test(bank.meta.updated)) {
      push('meta.updated debe tener formato YYYY-MM-DD.');
    }
  }

  // --- jugabilidad ----------------------------------------------------------
  if (bank.config && Number.isInteger(bank.config.questionsPerGame)) {
    if (bank.questions.length < bank.config.questionsPerGame) {
      push(`El banco (${bank.questions.length}) no alcanza para una partida de ${bank.config.questionsPerGame}.`);
    }
  }

  return errors;
}

module.exports = { validate, latexBalanced, countPerLevel, levelSizes, niceRound };
