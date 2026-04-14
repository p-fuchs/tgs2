# Deep research report (reconstructed export)

## Executive summary

This package captures the content of the deep research plan for a 45-minute presentation on **“Women’s connectivity in extreme networks”** by Manrique et al. (Science Advances, 2016).

Recommended talk shape:
- 23 core slides including Q&A
- ~38 minutes of presentation
- ~7 minutes for questions
- ~5 backup slides

Narrative arc:
1. Motivation and research question
2. Two operational networks: online pro-ISIS VKontakte network and offline PIRA collaboration network
3. Two centrality measures: degree and betweenness
4. Main empirical results: women exhibit higher betweenness; women avoid “star” visibility
5. Longevity associations
6. Interpretation, limitations, and careful implications

Visual strategy:
- Use the paper’s main figures as anchor visuals on the result slides
- Add a few custom visuals for pedagogy:
  - roadmap flowchart
  - hub vs broker cartoon
  - data construction pipeline
  - model assumptions flow

## Core paper facts to foreground

### Paper-level claim
The paper challenges the stereotype that women play only minor roles in dangerous, aggressive environments. Across both an online pro-ISIS support network and an offline PIRA operational network, the authors argue that women show superior **collective connectivity**, especially via betweenness centrality.

### Online network
- Platform: VKontakte
- Node meaning: individuals following pro-ISIS group pages
- Edge meaning: two people are linked if they follow the same group page on the same day
- Scale reported in the paper:
  - 41,880 total individuals
  - 24,883 men
  - 16,931 women
  - 66 undeclared
  - 170 groups
  - >1,000,000 aggregated links

### Offline network
- Case: PIRA
- Node meaning: PIRA actors
- Edge meaning: collaboration on an IED event / planned or executed assault within a given year
- Scale reported in the paper:
  - 926 different individuals over time
  - about 5% women
  - total registered members: 1382 (1312 men, 70 women)

### Central numerical results that should be said aloud
- In the online case, women’s average BC shows repeated large peaks relative to men.
- In the online case, women’s average degree centrality is significantly above a gender-shuffle null model.
- Reported Z-scores for degree centrality:
  - men: about -4.7
  - women: about +4.7
- In the offline PIRA case:
  - women’s BC rises above men’s over time
  - women’s degree centrality decreases faster than men’s
- Longevity result:
  - online groups with more women tend to live longer
  - reported Pearson r = 0.28, P < 0.1
- Offline longevity result:
  - actors directly connected to women have longer average lifetimes than actors directly connected to men and to a shuffled-gender null model

## Design system for the deck

### Aspect ratio
Use 16:9.

### Density rule
One major idea per slide. The densest slides are the result slides built around the paper’s own figures.

### Typography rule
Large titles, short bullets, and wide margins. Prefer spoken explanation over full-sentence text walls.

### Colour logic
Use one stable colour mapping for the whole deck:
- blue: men
- red/orange: women
- gray: null model / background / non-focal nodes

### Reusable layout patterns
1. **Figure-right layout**
   - left: 2–3 bullets and one interpretation box
   - right: the paper figure as the hero visual

2. **Two-concept comparison**
   - left and right balanced panels
   - ideal for “hub vs broker” and “degree vs betweenness”

3. **Flowchart slide**
   - full-width TikZ-style or drawn diagram
   - use only when the visual is itself the explanation

4. **Takeaway slide**
   - no more than three numbered takeaways
   - one short “open questions” box

## Timing model

### Recommended allocation
- Slides 1–3: 3.5 minutes
- Slides 4–6: 6.5 minutes
- Slides 7–10: 7.5 minutes
- Slides 11–15: 9.5 minutes
- Slides 16–19: 7.0 minutes
- Slides 20–22: 4.0 minutes
- Slide 23 (Q&A): 7.0 minutes

## Slide-by-slide plan

---

### Slide 1 — Title
**Goal:** establish topic, paper, and tone.

**On-slide content**
- Title: *Women’s connectivity in extreme networks*
- Subtitle: based on Manrique et al. (Science Advances, 2016)
- Your name / venue / date

**Layout**
- Plain title slide
- Optional tiny network icon in a corner
- Keep empty space; do not crowd it

**Speaker note**
- “This talk is based almost entirely on one paper.”
- “We’ll compare two extreme operational networks—one online, one offline.”
- “The key idea is that who matters depends on what notion of centrality you use.”

**Visual**
- None required beyond minimal title treatment

---

### Slide 2 — Motivation: who is central in extreme networks?
**Goal:** introduce the paper’s framing and question.

**On-slide content**
- Stereotype: women are assumed to play minor roles in dangerous environments
- Paper’s question: does network position contradict this?
- Settings: pro-ISIS online support network and PIRA operational network

**Layout**
- 55/45 split
- left: problem framing bullets
- right: callout box with the core claim

**Speaker note**
- Contrast local visibility with collective importance
- Say explicitly that the talk is about **network roles**, not celebrity or notoriety

**Visual**
- A single question-box graphic:
  “Who holds the network together under pressure?”

---

### Slide 3 — Paper roadmap
**Goal:** give the audience a map.

**On-slide content**
- Introduction / question
- Data sets
- Online results
- Offline results
- Longevity
- Discussion / limitations

**Layout**
- Full-width roadmap flowchart
- Six boxes linked top-to-bottom or branching at the data stage

**Speaker note**
- Promise the audience that the result slides will follow the paper’s structure closely

**Visual**
- Custom flowchart

---

### Slide 4 — Degree vs betweenness centrality
**Goal:** give the minimum theory needed.

**On-slide content**
- Degree centrality = local visibility / number of neighbours
- Betweenness centrality = fraction of shortest paths through a node
- Include the paper’s BC formula and normalized BC formula

**Layout**
- 55/45 split
- left: formula + symbol definitions
- right: hub vs bridge cartoon

**Speaker note**
- Explain why shortest paths matter in covert networks: more hops mean more risk / more cost
- The audience must leave this slide understanding why someone can have low degree but high betweenness

**Visual**
- Custom hub-vs-bridge diagram

---

### Slide 5 — Data sets at a glance
**Goal:** compare the two empirical settings cleanly.

**On-slide content**
A compact comparison table with:
- nodes
- edges
- time resolution
- reported scale

**Layout**
- top: comparison table
- bottom: simple timeline strip for PIRA chronology

**Speaker note**
- Stress that these are **operational ties**, not friendship ties
- Explain the difference in time resolution: daily online vs yearly offline

**Visual**
- Comparison table + small timeline strip

---

### Slide 6 — Online network construction pipeline
**Goal:** make the VKontakte network construction legible.

**On-slide content**
Five-step identification procedure from the paper:
1. manual hashtag / narrative search
2. seed group pages
3. API-based snowballing
4. cross-check and removal of false positives
5. iterate to closure

Then:
- daily edge rule: connect people who follow the same pro-ISIS group page on that day

**Layout**
- two columns
- left: numbered steps
- right: flowchart

**Speaker note**
- Mention that closure is important
- Mention that the daily network changes in both nodes and links

**Visual**
- Custom pipeline flowchart

---

### Slide 7 — Online pro-ISIS daily snapshots (Figure 1A)
**Goal:** show that the online network is dynamic.

**On-slide content**
- Three short bullets explaining how to read the snapshots

**Layout**
- figure-right layout
- left: reading instructions
- right: Figure 1A composite

**Speaker note**
- Emphasize: centrality is computed on a changing daily network, not a static graph

**Visual**
- `figures/figure1_composite.png` or the first panel of Figure 1

---

### Slide 8 — Online result: women show higher betweenness peaks (Figure 1B)
**Goal:** present the first key result.

**On-slide content**
- x-axis = day
- y-axis = average BC
- women’s curve/spikes exceed men’s repeatedly

**Layout**
- figure-right layout

**Speaker note**
- Explain operational meaning:
  women can sit on more shortest-path routes
- Use the paper’s interpretation: brokerage for messages, files, propaganda, funds, and distant-network coordination

**Visual**
- panel B of Figure 1

---

### Slide 9 — Online result: degree centrality and null model (Figure 1C)
**Goal:** show that the effect is not only anecdotal and introduce the null model.

**On-slide content**
- null model = shuffle genders across the fixed network
- women’s degree centrality is significantly above null
- reported Z-scores: women +4.7, men -4.7

**Layout**
- left: null-model explanation and Z-score reminder
- right: figure

**Speaker note**
- Clarify what the null does and does not test
- Make the point that topology is fixed; only gender labels are permuted

**Visual**
- panel C of Figure 1

---

### Slide 10 — Mechanism intuition: avoid “stars,” retain brokerage (Figure 1D)
**Goal:** make the degree/BC distinction memorable.

**On-slide content**
- Left concept: high BC + high degree = visible star
- Right concept: high BC + low degree = broker / bridge
- Bottom-line takeaway:
  women can deliver global network value while avoiding conspicuous hub status

**Layout**
- symmetric two-panel slide

**Speaker note**
- This is the key interpretive hinge of the online case
- Slow down here; this slide makes the rest of the talk easier

**Visual**
- panel D of Figure 1 or a clean redraw

---

### Slide 11 — Offline PIRA network construction
**Goal:** define the offline network carefully.

**On-slide content**
- nodes = PIRA actors
- yearly edge if actors collaborated on an IED event or assault
- archival / coded event data
- reported scale numbers

**Layout**
- figure-right layout
- right: snapshot panel from Figure 2A

**Speaker note**
- Explain why the offline setting matters:
  risk is direct, on-street, and materially dangerous

**Visual**
- panel A of Figure 2

---

### Slide 12 — PIRA productivity rises without actor growth (Figure 2B)
**Goal:** motivate why structure matters, not just size.

**On-slide content**
- IED attacks rise over time
- actor counts do not rise in parallel

**Layout**
- figure-right layout

**Speaker note**
- Say explicitly that this undermines the simplistic story “more productivity = more people”
- Transition to structural roles

**Visual**
- panel B of Figure 2

---

### Slide 13 — Offline result: women’s betweenness rises above men’s (Figure 2C)
**Goal:** show the cross-setting recurrence of the BC finding.

**On-slide content**
- women’s BC rises over time to values well above men’s

**Layout**
- figure-right layout

**Speaker note**
- Highlight the replication logic:
  a similar BC pattern appears in a very different environment

**Visual**
- panel C of Figure 2

---

### Slide 14 — Offline result: women’s degree centrality declines faster (Figure 2D)
**Goal:** show the sharper visibility-avoidance pattern offline.

**On-slide content**
- degree centrality decreases for both
- women’s decline is faster

**Layout**
- figure-right layout

**Speaker note**
- Offer the paper’s cautious interpretation:
  higher direct risk may make lower local visibility even more valuable offline

**Visual**
- panel D of Figure 2

---

### Slide 15 — Model interlude: fission–fusion + team ethic (Figure 2E)
**Goal:** present the modelling move without overselling it.

**On-slide content**
- authors temporarily assume:
  1. high-BC actors are more team-player oriented
  2. that team ethic spreads inside clusters containing women
  3. this operates on top of fission–fusion dynamics
- simulation reproduces two summary features of the PIRA data

**Layout**
- top: assumptions flow diagram
- bottom: Figure 2E

**Speaker note**
- Be explicit that this is a stylized model, not a proven causal mechanism
- Use the phrase “notional mechanism” or equivalent

**Visual**
- custom assumptions flow + panel E of Figure 2

---

### Slide 16 — Online longevity: more women, longer-lived groups (Figure 3A)
**Goal:** introduce the robustness / survival association.

**On-slide content**
- group lifetime tends to increase with women/men ratio
- report Pearson r = 0.28, P < 0.1

**Layout**
- figure-left, statistics box on the right

**Speaker note**
- Stress association, not causation
- Mention external shutdowns by platforms / outside agents

**Visual**
- panel A of Figure 3

---

### Slide 17 — Offline longevity: neighbours of women persist longer (Figure 3B)
**Goal:** show the offline longevity analogue.

**On-slide content**
- actors directly connected to women have longer average lifetimes
- also above a shuffled-gender null model

**Layout**
- figure-right layout

**Speaker note**
- Translate this into network language:
  women appear better embedded in resilient structures

**Visual**
- panel B of Figure 3

---

### Slide 18 — Alternative explanations discussed in the paper
**Goal:** show that the authors stress-tested their own interpretation.

**On-slide content**
Checklist of alternatives:
- incomplete networks
- exceptional women / outliers
- role monopolisation
- higher-order statistics issue
- women naturally attracting more attention online

**Layout**
- left: alternatives checklist
- right: short evidence/counterpoint box

**Speaker note**
- Present this as a credibility slide
- “Here is what the paper itself worries about.”

**Visual**
- optional icon list or checkmark/warning grid

---

### Slide 19 — Limitations and validity boundaries
**Goal:** define what the paper does not claim.

**On-slide content**
Three blocks:
1. data limitations
2. measurement limitations
3. inference discipline

**Layout**
- stacked block slide

**Speaker note**
- Say explicitly:
  “This supports claims about topological role, not psychological intent.”

**Visual**
- minimal; the structure itself should do the work

---

### Slide 20 — Implications: rethinking “importance”
**Goal:** connect the results to evaluation and intervention logic at a high level.

**On-slide content**
- hub-centric strategies focus on degree
- this paper suggests attention to brokerage and women’s interconnectivity
- do not frame this as targeting; frame it as understanding and engagement

**Layout**
- left: implication paragraph in bullets
- right: hub-centric vs broker-centric contrast graphic

**Speaker note**
- Keep the language responsible and abstract
- Focus on measurement and network evaluation

**Visual**
- custom contrast diagram

---

### Slide 21 — Ethics and responsible communication
**Goal:** control framing for a sensitive topic.

**On-slide content**
- This talk is about network science, not operational advice
- Avoid reproducing extremist media beyond abstracted network figures
- Be explicit about uncertainty and non-causal interpretation

**Layout**
- alert block + checklist

**Speaker note**
- Brief but important
- This slide should feel principled, not defensive

**Visual**
- optional minimal ethics guardrail icon

---

### Slide 22 — Conclusions and open questions
**Goal:** end with three durable takeaways.

**On-slide content**
1. women show higher betweenness in both networks studied
2. degree and betweenness diverge; women can avoid “star” visibility while still bridging
3. longevity patterns are consistent with system-level consequences of women’s embedding

Open questions:
- how general is the pattern?
- how does pressure change centrality?
- how should contributions be evaluated: local visibility or collective connectivity?

**Layout**
- top: three numbered takeaways
- bottom: open-questions box

**Speaker note**
- Keep it crisp
- The audience should be able to photograph this slide and remember the whole talk

**Visual**
- none necessary

---

### Slide 23 — Q&A
**Goal:** leave explicit room for questions.

**On-slide content**
- “Q&A”
- “Backup slides available”

**Layout**
- plain, centered

**Speaker note**
- If needed, jump to backups on BC intuition, null model, dataset magnitudes, or supplementary figures

---

## Backup slides

### Backup A1 — Why betweenness matters
- Freeman-style shortest-path intuition
- use a minimal three-node bridge diagram

### Backup A2 — Null model logic
- what stays fixed
- what is randomized
- what conclusion the null supports

### Backup A3 — Dataset magnitudes
- online and offline counts
- useful for methods questions

### Backup A4 — Supplementary figures placeholder
- fig. S1: BC intuition
- fig. S2: productivity not driven by more actors
- fig. S3: generative model schematic
- fig. S4: not just a few exceptional women
- fig. S5: BC not tied clearly to one operational role

### Backup A5 — References
- one slide or appendix frame with references

## Asset checklist from the deep research plan

Main paper figures to use:
- Figure 1: online results
- Figure 2: offline results + model
- Figure 3: longevity

Recommended custom visuals:
- roadmap flowchart
- degree vs betweenness cartoon
- VKontakte data collection pipeline
- model assumptions flow
- implication contrast (hub-centric vs broker-centric)

## Bibliography starter

```bibtex
@article{Manrique2016WomenConnectivity,
  author  = {Manrique, Pedro and Cao, Zhenfeng and Gabriel, Andrew and Horgan, John and Gill, Paul and Qi, Hong and Restrepo, Elvira M. and Johnson, Daniela and Wuchty, Stefan and Song, Chaoming and Johnson, Neil},
  title   = {Women's connectivity in extreme networks},
  journal = {Science Advances},
  year    = {2016},
  volume  = {2},
  number  = {6},
  pages   = {e1501742},
  doi     = {10.1126/sciadv.1501742}
}

@article{Freeman1977Betweenness,
  author  = {Freeman, Linton C.},
  title   = {A Set of Measures of Centrality Based on Betweenness},
  journal = {Sociometry},
  year    = {1977},
  volume  = {40},
  number  = {1},
  pages   = {35--41}
}
```

## Figure extraction notes

The ZIP includes three extracted figure composites from the uploaded paper:
- `figure1_composite.png`
- `figure2_composite.png`
- `figure3_composite.png`

These were cropped from full rendered page images of the uploaded PDF and are intended for presentation drafting rather than publication-quality republication.

