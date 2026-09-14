/**
 * Paleta de símbolos del Tablero LaTeX.
 * Cada item usa `$0` como marcador de posición del cursor al insertar.
 */
export const groups = [
  {
    id: 'basico',
    label: 'Básico',
    items: [
      ['x^2', 'x^{$0}'], ['x_i', 'x_{$0}'], ['a/b', '\\frac{$0}{}'],
      ['√', '\\sqrt{$0}'], ['ⁿ√', '\\sqrt[n]{$0}'], ['( )', '\\left( $0 \\right)'],
      ['[ ]', '\\left[ $0 \\right]'], ['{ }', '\\left\\{ $0 \\right\\}'],
      ['·', '\\cdot '], ['×', '\\times '], ['÷', '\\div '], ['±', '\\pm '],
      ['%', '\\%'], ['|x|', '\\left| $0 \\right|'],
    ],
  },
  {
    id: 'griego',
    label: 'Griego',
    items: [
      ['α β γ', '\\alpha \\beta \\gamma '], ['δ ε', '\\delta \\epsilon '],
      ['θ λ μ', '\\theta \\lambda \\mu '], ['ν ρ σ', '\\nu \\rho \\sigma '],
      ['τ φ π', '\\tau \\phi \\pi '], ['Γ Δ', '\\Gamma \\Delta '],
      ['Θ Λ', '\\Theta \\Lambda '], ['Π Σ', '\\Pi \\Sigma '],
      ['Φ Ψ Ω', '\\Phi \\Psi \\Omega '],
    ],
  },
  {
    id: 'operadores',
    label: 'Operadores',
    items: [
      ['Σ', '\\sum_{i=1}^{$0}'], ['Π', '\\prod_{i=1}^{$0}'], ['∫', '\\int_{a}^{b} $0 \\,dx'],
      ['∮', '\\oint $0'], ['lim', '\\lim_{x \\to \\infty} '], ['d/dx', '\\frac{d}{dx}\\left( $0 \\right)'],
      ['∂', '\\partial '], ['∇', '\\nabla '], ['∞', '\\infty '], ['≤ ≥', '\\leq \\geq '],
      ['≠ ≈', '\\neq \\approx '], ['≡ ∼', '\\equiv \\sim '], ['∈ ∉', '\\in \\notin '],
      ['⊂ ⊆', '\\subset \\subseteq '], ['∀ ∃', '\\forall \\exists '],
    ],
  },
  {
    id: 'flechas',
    label: 'Flechas',
    items: [
      ['→', '\\to '], ['←', '\\leftarrow '], ['↔', '\\leftrightarrow '],
      ['⇒', '\\Rightarrow '], ['⇔', '\\Leftrightarrow '], ['⟹', '\\Longrightarrow '],
      ['↦', '\\mapsto '], ['↑ ↓', '\\uparrow \\downarrow '],
    ],
  },
  {
    id: 'logica',
    label: 'Lógica / Conjuntos',
    items: [
      ['∧ ∨ ¬', '\\land \\lor \\lnot '], ['∪ ∩', '\\cup \\cap '], ['∅', '\\emptyset '],
      ['ℝ', '\\mathbb{R}'], ['ℕ', '\\mathbb{N}'], ['ℤ', '\\mathbb{Z}'],
      ['ℚ', '\\mathbb{Q}'], ['ℂ', '\\mathbb{C}'], ['𝔼', '\\mathbb{E}'],
      ['ℙ', '\\mathbb{P}'], ['ℒ', '\\mathcal{L}'], ['𝒩', '\\mathcal{N}'],
    ],
  },
  {
    id: 'estructuras',
    label: 'Estructuras',
    items: [
      ['b(n,k)', '\\binom{n}{k}'], ['x̄', '\\bar{x}'], ['x̂', '\\hat{x}'],
      ['x̃', '\\tilde{x}'], ['x⃗', '\\vec{x}'], ['x‾', '\\overline{x}'],
      ['texto', '\\text{$0}'],
      ['matriz', '\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}'],
      ['casos', '\\begin{cases} a & x > 0 \\\\ b & x \\leq 0 \\end{cases}'],
      ['align', '\\begin{align} a &= b \\\\ c &= d \\end{align}'],
      ['conjunto', '\\left\\{ x \\in \\mathbb{R} : $0 \\right\\}'],
    ],
  },
  {
    id: 'formato',
    label: 'Color / Tamaño',
    items: [
      ['verde', '\\textcolor{#6c9a06}{$0}'], ['teal', '\\textcolor{#0e7774}{$0}'],
      ['rojo', '\\textcolor{#dc2626}{$0}'], ['ámbar', '\\textcolor{#f59e0b}{$0}'],
      ['display', '\\displaystyle $0'], ['\\big', '\\bigl( $0 \\bigr)'],
      ['\\Big', '\\Bigl( $0 \\Bigr)'], ['negrilla', '\\mathbf{$0}'],
      ['bold', '\\boldsymbol{$0}'], ['caja', '\\boxed{$0}'],
    ],
  },
];

export const defaultTex = String.raw`\begin{align}
\mathbb{E}(X) &= \sum_{i=1}^{n} x_i \, p(x_i) \\
\operatorname{Var}(X) &= \mathbb{E}(X^2) - \left[\mathbb{E}(X)\right]^2
\end{align}`;
