# Technical style and LaTeX

Apply these conventions when they do not conflict with the venue template or the repository's established style.

## Sentence and paragraph style

- Put the paragraph's main point first and give the paragraph one primary job.
- Describe a phenomenon with the shortest sentence that remains accurate. State what happened before explaining why it happened.
- Prefer concrete subjects and verbs: “The bound scales with $d$” is clearer than “A dependence on $d$ can be observed.”
- Use the same precise term for the same concept. Do not rotate synonyms for variety when readers may infer a technical distinction.
- Keep formulas grammatically integrated into sentences. Add punctuation after displayed equations.
- Avoid beginning a sentence with a symbol when a short noun phrase would orient the reader.
- Avoid contractions and unexplained colloquialisms in formal prose.
- Use hyphens in compound modifiers: “$(d-k)$-dimensional,” “real-world data,” and “ground-truth label,” but “the ground truth.”
- Use the Oxford comma consistently.
- Check articles, singular/plural agreement, and subject--verb agreement, especially in long sentences around citations.
- Break a long sentence when it carries multiple logical relationships. Short does not mean choppy: preserve explicit transitions.

For a phenomenon sentence, prefer the structure “object + change or relation.” Put setup, mechanism, evidence, and caveats in later sentences unless a qualifier is required to make the first sentence true. Do not optimize for raw word count at the expense of scope, uncertainty, or mathematical correctness.

When introducing a difficult idea, choose the order that minimizes reader effort. A concrete example may precede intuition; intuition should normally precede formalism; the formal statement should be followed by interpretation.

## Terminology and macros

Choose a small set of names for the paper's key concepts early. Maintain a terminology sheet if several authors are editing. Use semantic LaTeX macros for:

- method and dataset names;
- mathematical objects or operators;
- notation likely to change;
- repeated formatting distinctions.

Do not hide ordinary prose behind macros. A macro should improve consistency or maintainability.

## Equations

- Use `align` for genuine multi-line derivations and align at the logical relation.
- Label equations or individual lines that will be referenced. Suppress numbering only for lines that have no later identity.
- When a line uses a theorem or transformation that is not obvious, put a short explanation close to that line. A compact annotation is better than forcing the reader to match “line 3” with a later paragraph.
- Avoid `$$...$$`; it does not integrate well with document numbering and spacing.
- Define important quantities before displaying an equation that depends on them. A trailing “where” clause is fine for secondary or familiar symbols.
- Use `\mathrm{}` or `\operatorname{}` for named operators and semantic macros for recurring special quantities.
- Prefer explicit delimiter sizing such as `\bigl` and `\bigr` when automatic `\left` and `\right` produces distracting sizes.
- Use words for trivial pseudocode operations when symbols make them harder to parse, for example “add $a$ to $S$.”

## Theorem and equation numbering

For theorem-heavy papers, a shared counter for theorems, lemmas, propositions, and corollaries often reduces ambiguity. Number statements and equations by section when the venue and existing source permit it. Definitions may use the same counter unless a separate sequence clearly helps.

Every theorem, lemma, and claim should have a proof immediately afterward or a precise pointer to its proof. Use a `proof` environment; when the statement is not adjacent, name it in the optional proof heading.

## Figures and captions

Treat each figure as one idea.

- Begin the caption with a bold or otherwise visually clear takeaway sentence when the template allows.
- Explain panels, colors, axes, metrics, units, and comparison conditions.
- State what the reader should conclude, while distinguishing observation from interpretation.
- Make the caption self-contained enough for an expert skimming only figures.
- Use the same axis limits for directly comparable plots unless a different scale is necessary and clearly marked.
- Choose convenient units such as thousands or millions instead of long strings of zeros.
- Check font, legend, label, and line sizes at the figure's final paper dimensions.

Plot trends when the trend is the message; use tables when exact values or many categorical comparisons matter.

## Citations

With `natbib`, use `\citep{}` for parenthetical citations and `\citet{}` when the citation is grammatically part of the sentence. Removing a `\citep{}` should leave a valid sentence; removing a `\citet{}` generally should not.

Maintain grammatical agreement. “Smith et al. show” refers to authors; “the work of Smith et al. shows” refers to a work. When discussing a limitation, target the exact result or assumption: “Theorem 2 requires X” is more precise and collegial than a broad claim about the authors.

Verify bibliographic data against the published version when available. Do not invent citation keys or references. Preserve existing keys unless there is a strong repository reason to change them.

## Source organization

For a multi-section LaTeX paper, prefer a small main entry point—commonly `main.tex`—that loads a shared macro/style file and inputs one source file per substantial section. Follow the current repository if it already uses another organization.

Avoid large regions disabled with `\iffalse...\fi`; version control and small comments are easier to edit and review. Preserve unresolved coauthor comments unless the user explicitly asks to remove them. Resolve only comments that are clearly addressed, and do not erase uncertainty that still needs author review.
