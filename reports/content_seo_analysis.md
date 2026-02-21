# Content & SEO Analysis: /info, WRITING.txt, and Funnel Guides

## 1. What “/info” Means in This Project

**There is no `/info` URL or page in the repo.** Current top-level routes include:

- `/` (home)
- `/about/`, `/blog/`, `/contact/`, `/portfolio/`
- `/residential-landscaping/`
- `/services/*`, `/commercial-*`, `/locations/*`

So “/info” is treated here in two ways:

- **If you mean a real URL:** You could add a dedicated **informational hub** (e.g. permalink `/info/` or `/resources/`) that holds TOFU content (guides, how-tos, FAQs). That would align with the Terakeet funnel model and give a clear place for “awareness” content.
- **If you mean “informational content” in general:** That’s **TOFU** in the Terakeet guide—blog posts, how-tos, guides, FAQs. Your blog and service pages already play that role; the gap is having a clear **TOFU → MOFU → BOFU** path and content types spelled out per stage.

---

## 2. WRITING.txt (Master Copywriting Operator)

**Role:** Defines how copy is produced—headlines, structure (AIDA), editing, readability, A/B variants, and the “Professor Cyrus” brainstorming flow.

**Relevance to the two guides:**

| Guide | Connection to WRITING.txt |
|-------|---------------------------|
| **Terakeet (TOFU/MOFU/BOFU)** | WRITING.txt is **stage-agnostic**. It doesn’t say “use AIDA only on BOFU” or “use HEADLINE MODE for TOFU.” To align with the funnel, you’d **assign modes by stage**: e.g. TOFU = READABILITY + curiosity/educational tone; MOFU = AIDA + EDIT (comparisons, trust); BOFU = AIDA + strong CTA, A/B VARIANT MODE for landing/quote pages. |
| **Neil Patel (AnswerThePublic + AI prompts)** | “Specificity” and “Use of Keywords” in the Neil guide match WRITING.txt’s “Clear. Persuasive. Tight” and “Avoid fluff.” Better prompts (e.g. seeded with AnswerThePublic questions) produce better input for any WRITING.txt mode. So: **keyword/question research first → then run WRITING.txt (headline, AIDA, edit) on that brief.** |

**Practical alignment:**

- Use **WRITING.txt** as the **copy execution layer** (how to write).
- Use **Terakeet** as the **content strategy layer** (what to write at which funnel stage).
- Use **Neil Patel’s method** (AnswerThePublic, user intent, seed questions) as the **research layer** that feeds both: topics, questions, and intent so WRITING.txt outputs are on-target and SEO-aware.

---

## 3. Terakeet Guide: TOFU, MOFU, BOFU

**Summary:** The buyer journey is split into Awareness (TOFU), Consideration (MOFU), Decision (BOFU). Search behavior and content needs differ by stage; SEO and content should be optimized per stage.

**Applied to Serene Landscaping:**

| Stage | Search / intent | Content types (from guide) | What you already have | Gaps / opportunities |
|-------|------------------|----------------------------|------------------------|----------------------|
| **TOFU** | Broad, problem-aware (“lawn problems,” “when to install sod”) | Blog posts, guides, how-tos, FAQs, videos | Blog (e.g. spring lawn care, retaining wall cost, mulch, etc.) | Optional: dedicated hub (e.g. `/info/` or `/resources/`) to group TOFU content; more “how to” / “what is” articles from question research. |
| **MOFU** | Solution-aware, comparing (“best landscaper Edmonton,” “sod vs seed”) | Comparison content, benefits, case studies, webinars | Service pages (benefits, scope); some blog posts | Stronger MOFU: “X vs Y,” “best [service] Edmonton,” “cost of [project]” posts; clearer CTAs from blog to service/quote. |
| **BOFU** | Ready to act; branded or “near me” | Demos, trials, pricing, guarantees, CTAs | Contact, “Get a Free Quote,” trust bar (quote in 24h, no deposit) | Ensure every service page and location page has one clear primary CTA and trust (e.g. warranty, testimonials) near the CTA. |

**Website architecture (from the guide):**  
Internal links and nav should create a clear path: TOFU (blog/resources) → MOFU (service/commercial pages) → BOFU (contact/quote). Your breadcrumbs and service links already support this; adding an `/info/` or “Resources” section could make the TOFU→MOFU path more explicit.

---

## 4. Neil Patel Guide: AnswerThePublic + AI Prompts

**Summary:** Better AI output requires better prompts. AnswerThePublic (and similar tools) surface real search questions and themes; use those to make prompts **specific**, **keyword-aware**, and **intent-aware**. Refine prompts over time.

**Applied to Serene + WRITING.txt:**

- **Seed questions:** Use AnswerThePublic (or Ubersuggest, etc.) with seeds like “landscaping Edmonton,” “sod installation,” “snow removal Edmonton,” “retaining wall cost.” Export “question” phrases (who, what, when, where, why, how, is, can, etc.) and use them in:
  - **TOFU content:** Blog titles and H2s that match questions.
  - **AI prompts:** e.g. “Write a short, clear answer to: [exact question]. Audience: Edmonton homeowners. Tone: helpful, no jargon. Under 100 words.”
- **Key concepts:** Group autocomplete/prepositions (e.g. “landscaping *for*,” “sod *cost*,” “snow removal *commercial*”) to see themes (cost, timing, commercial vs residential). Feed those into WRITING.txt HEADLINE MODE or AIDA MODE so copy matches how people search.
- **User intent:** “Near me” / “cost” / “best” → BOFU or MOFU. “How to” / “what is” → TOFU. Tag content by intent and funnel stage so you don’t oversell on TOFU or under-sell on BOFU.
- **Refining prompts:** Reuse and tune prompts (e.g. “Edmonton landscaping FAQ answer”) and refresh keyword/question data periodically so WRITING.txt outputs stay aligned with current search behavior.

---

## 5. Synthesis: How the Three Fit Together

1. **Research (Neil Patel):** Use AnswerThePublic (or similar) to get seed keywords, questions, and themes for Edmonton landscaping, snow removal, sod, retaining walls, etc. Capture intent (informational vs commercial vs transactional).
2. **Strategy (Terakeet):** Map that research to TOFU / MOFU / BOFU. Decide what to create at each stage (e.g. TOFU: “How to prepare for sod,” MOFU: “Sod vs seed Edmonton,” BOFU: service pages + contact).
3. **Execution (WRITING.txt):** Use the right mode for the stage (e.g. READABILITY + curiosity for TOFU; AIDA + CTA for BOFU). Feed in the specific questions and keywords from step 1 so headlines and body copy are SEO- and intent-aligned.
4. **Optional: “/info” as a place:** If you add an `/info/` (or `/resources/`) page, use it as the TOFU hub: links to guides, FAQs, and blog posts, with clear paths from each piece to MOFU (service pages) and BOFU (contact/quote).

---

## 6. Quick Wins

- **llms.txt:** Already gives a concise service and contact brief. Keep it updated so any AI-assisted copy (via WRITING.txt or tools) stays on-brand and accurate.
- **WRITING.txt:** Add one line per mode suggesting funnel stage (e.g. “BOFU: prefer AIDA + strong CTA”) so operators know when to use which mode.
- **Content:** Run AnswerThePublic (or equivalent) for 3–5 core terms (e.g. “landscaping Edmonton,” “sod installation,” “snow removal Edmonton”) and create a short “target questions” list for the next 5–10 blog or FAQ pieces.
- **Architecture:** If you add `/info/`, add it to the main nav or footer and link TOFU content there, with clear internal links from TOFU → service pages → contact.

---

*Analysis based on: project files (/info check, WRITING.txt, llms.txt, permalinks), Terakeet “ToFu MoFu BoFu” guide, and Neil Patel “How AnswerThePublic Can Supercharge AI Prompts.”*
