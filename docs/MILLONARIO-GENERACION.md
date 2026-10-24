# Guía de generación de preguntas — ¿Quién quiere ser millonario? (Ecoudea)

Con esta guía + el contenido de **una clase** del repo, cualquier IA debe
producir un parcial que pase el validador `scripts/check-millonario.cjs`
a la primera. Todo se valida, nada se confía.

---

## 1. Pipeline (cómo entra una pregunta al juego)

```
1. La IA genera → data/millonario-src/<curso>-<clase>.json  (ver §2)
2. node scripts/build-millonario.cjs          (fusiona, asigna ids mq-NNN, ordena por nivel)
3. node scripts/check-millonario.cjs          (gate: 0 errores = válido)
4. El consolidado public/assets/data/millonario.json ya sirve al juego — no editarlo a mano
```

- **Añadir preguntas = añadir un parcial y correr el build.** Cero cambios de código.
- Nunca incluyas `id` en un parcial: lo asigna el build.
- Nunca edites `public/assets/data/millonario.json` a mano: se regenera.

## 2. Esquema del parcial (exacto)

Archivo único por clase: `data/millonario-src/<class>.json`, donde `<class>`
es el nombre del archivo de la clase SIN extensión (ej.
`macroeconomia-i-clase-03`). Debe existir en `src/content/classes/`.

```json
{
  "class": "macroeconomia-i-clase-03",
  "category": "macroeconomia",
  "questions": [
    {
      "difficulty": 1,
      "question": "Enunciado con $matemática$ inline si hace falta",
      "options": ["opcion A", "opcion B", "opcion C", "opcion D"],
      "correct": 0,
      "explanation": "Justificación breve y correcta, cite fórmulas si aplica"
    }
  ]
}
```

Reglas de los campos:

| Campo | Regla |
|---|---|
| `class` | nombre real de la clase en `src/content/classes/` (sin `.md`). Obligatorio. |
| `category` | `macroeconomia` \| `estadistica` (el esquema admite otras sin cambios de código) |
| `difficulty` | entero 1–5 (rúbrica en §4). Se exigen ≥ 3 preguntas por nivel en el banco. |
| `question` | 10–400 caracteres, una sola línea, MATLAB… perdón, LaTeX con `$...$` balanceado |
| `options` | **exactamente 4** cadenas (2–220 caracteres). Prohibido “todas las anteriores” / “ninguna de las anteriores” y duplicados. |
| `correct` | índice 0–3 de la option correcta (siempre `0` en los parciales; el juego baraja) |
| `explanation` | 10+ caracteres, LaTeX balanceado. Explica POR QUÉ es correcta y por qué no las otras. |

Validaciones automáticas (gate): JSON válido · 4 opciones · exactamente 1
correcta · ids únicos (los asigna el build) · dificultad 1–5 · ≥3 por nivel ·
`source` = clase existente · `$` pares en cada campo · sin opciones
duplicadas · sin “todas/ninguna de las anteriores” · longitudes razonables ·
enunciados sin duplicar.

## 3. LaTeX en los textos

- Inline: `$SCT = SCR + SCE$`, `$\beta(1+r)\,u'(C_2)$`. Cada `$` abre y cierra:
  si el campo tiene `$` impares, el check **falla**.
- Display: permitido con `$$...$$` solo si aporta (p. ej. una igualdad larga).
  Los `$` de display se excluyen del conteo de parity; los sueltos no.
- Escapes JSON: toda barra invertida va doble en el archivo (`"\\beta"`).
- No uses `\tag` ni referencias: las preguntas son autocontenidas.

## 4. Rúbrica de dificultad (decide el nivel ANTES de redactar)

| Nivel | Qué mide | Ejemplo típico |
|---|---|---|
| 1 | Definición / recuerdo | “¿Qué representa $Y_{\ell t}$?” |
| 2 | Identificó una fórmula / regla del curso val viva | ley de movimiento, Ecuación de Euler, grados de libertad ANOVA |
| 3 | Aplicación con cálculo corto o lectura estructural | R² con $SCT$ y $SCE$ dados, reconocer la RPI completa, RMS = razón de precios |
| 4 | Cálculo multi-paso o consecuencia fin de un supuesto | despeje del activo, $\beta(1+r)=1 \Rightarrow C_1=C_2$, $R^2$ ajustado con variable irrelevante |
| 5 | Razonamiento multi-paso / interpretación económica | transversalidad, Jensen + suavizado, IC vs IP, potencia vs tipo II |

## 5. Reglas de buenos distractores

1. **Error conceptual plausible, no absurdo**: el distractor debe ser la
   respuesta que daría quien entiende a medias (invertir $\beta$ y
   $\beta(1+r)$, confundir SCR con SCE, olvidar el descuento del ingreso
   laboral).
2. **Mismo formato y longitud aprox.** que la correcta (misma estructura sintáctica).
3. **Sin claves que delatan**: nada de “ninguna de las anteriores”, nada de
   opciones ridículas de relleno, nada de estilos que rompetyl la simetría.
4. **Precisiones**: 3–4 distractores de un mismo concepto (no 4 temas distintos).
5. La `explanation` debe poder descartar a los 4 distractores en una frase.

## 6. Ejemplo completo (parcial mínimo, pasa el validador)

```json
{
  "class": "estadistica-ii-clase-01",
  "category": "estadistica",
  "questions": [
    {
      "difficulty": 3,
      "question": "Si en una regresión $SCT = 100$ y $SCE = 30$, el coeficiente de determinación $R^2$ vale...",
      "options": [
        "$0.7$",
        "$0.3$",
        "$1.3$",
        "$\\frac{SCE}{SCR} \\approx 0.43$"
      ],
      "correct": 0,
      "explanation": "$R^2 = SCR/SCT = 1 - SCE/SCT = 1 - 30/100 = 0.7$: el $70\\%$ de la variación de $Y$ queda explicado por la relación lineal con $X$."
    }
  ]
}
```

## 7. Prompt-plantilla (pegar tal cual a la IA, con el texto de la clase)

> Eres redactora de preguntas de un curso universitario. Con el CONTENIDO DE
> LA CLASE pegado abajo, genera SOLO JSON válido (sin markdown, sin
> fences, sin comentario) con este esquema EXACTO:
> `{"class": "<NOMBRE_ARCHIVO_SIN_.md>", "category": "<macroeconomia|estadistica>", "questions": [ ... ]}`.
>
> Etiqueta: responde únicamente con JSON y nada más (sin ```).
> Cada pregunta en `questions` tiene: `difficulty` (entero 1-5, rúbrica:
> 1 definición, 2 fórmula/regla, 3 cálculo corto, 4 multi-paso, 5
> razonamiento multi-paso), `question` (máx 400 caracteres, una línea),
> `options` (exactamente 4), `correct` (siempre 0: la correcta es la
> primera), `explanation` (explica por qué es correcta y por qué no las
> otras).
>
> REGLAS INVIOLABLES:
> - Toda pregunta debe ser JUSTIFICABLE con el texto de la clase: si un dato
>   no está ahí, no lo uses.
> - Cuando uses LaTex, escribe `$...$` balanceado en todo campo (e.g.
>   `$SCT$`). En JSON escapa las barras: `"\\beta"`.
> - PROHIBIDO usar opciones del tipo "todas las anteriores" / "ninguna de las anteriores".
> - Distractores por error conceptual plausible, misma longitud y formato
>   que la correcta.
> - 6 preguntas: 2 nivel 1-2 y 4 niveles 3-5 (mezcla los niveles).
> - Sin markdown, sin texto fuera del JSON.

---

## 8. Comprobación rápida (lo último que haces)

```
node scripts/build-millonario.cjs
node scripts/check-millonario.cjs
```

Ambos imprimen `OK`/`CHECK OK` con el resumen por nivel. Si sale rojo el
detalle `msg` te dice exactamente qué corregir (corre el parcial, nunca el consolidado).
