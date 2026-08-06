# Post Pattern

Use this pattern as a flexible house style. Omit empty subsections instead of forcing content.

## Title

Always use this form:

```text
[LeetCode 75 Day N] 문제번호. 문제 제목 & 문제번호. 문제 제목
```

For example:

```text
[LeetCode 75 Day 13] 11. Container With Most Water & 1679. Max Number of K-Sum Pairs
```

Rules:

- The bracketed prefix is always exactly `[LeetCode 75 Day N]` in that English form. Never write it as `알고리즘 스터디 N일차` or any other variant.
- `N` is the cumulative day count across all weeks, not the day number inside the week. Determine it from the repository layout and recent commit messages (for example `week2/day5` was Day 12, so `week2/day6` is Day 13).
- List every problem solved that day, in the order they appear in the post, joined by ` & `.
- Use each problem's original English title with its judge number, exactly as on LeetCode.
- Do not add a separate thematic phrase to the title. The shared theme belongs in the introduction, not the heading.

## Introduction

Write one or two short paragraphs covering:

- why the learner selected these problems;
- the broader learning goal;
- what felt unfamiliar or worth recording.

Keep first-person statements only when supported by the user's notes.

## Problem Sections

Create one numbered section per problem:

```markdown
## 1. Problem Title - 짧은 한국어 설명

문제를 한두 문장으로 설명한다.

```python
# verified final solution
```

핵심 아이디어를 자연스러운 문단으로 설명한다.

풀면서 걸렸던 부분은 다음과 같았다.

- 실제로 막혔던 문법, 논리, 플랫폼 차이

시간 복잡도는 `O(...)`, 공간 복잡도는 `O(...)`이다.

### 더 개선한다면

무엇이 아쉬운지 한 문단으로 짚는다.

```python
# 개선한 코드
```

무엇이 달라졌고 어떤 대가를 치렀는지 한두 문장으로 덧붙인다.
```

Explain the code in execution order. State why boundary cases work. Do not repeat every line mechanically.

## Improvement Reflection

Every problem section ends with a `### 더 개선한다면` subsection: a short reflection on how the accepted solution could still be improved, followed by an improved code block.

Pick an axis that is genuinely open for that problem, in roughly this order of preference:

1. **복잡도** — a lower time or space bound, or removing an unnecessary extra pass or buffer.
2. **파이썬다움** — replacing manual loops with `enumerate`, `zip`, comprehensions, `collections`, `itertools`, slicing, or built-ins, when it actually reads better.
3. **가독성과 구조** — clearer names, early returns, removing duplicated branches, splitting a helper.
4. **일반화와 견고함** — handling inputs the judge happens not to test, or extending the idea to a `k`-sized version of the problem.

Rules:

- The improved code must be verified the same way as the main solution. Never present untraced code as improved.
- The improved code must actually differ from the solution above it. If nothing meaningful changes, do not print a near-identical block.
- If the solution is already optimal in complexity, say so plainly and improve a different axis. Do not invent a faster algorithm that does not exist.
- State the trade-off honestly when there is one, such as shorter code that hides the loop's intent, or lower space at the cost of mutating the input.
- Keep it to one or two paragraphs plus one code block. This is a closing note, not a second full solution walkthrough.
- If an improvement changes the complexity, restate the new complexity.
- Prefer improvements the learner could plausibly have reached from their own code, and connect them to the stumbling points named above when the link is real.

## Self Q&A

When the source contains several genuine questions, add:

```markdown
## N. 스스로 묻고 답한 질문들

### Q. 질문

답변
```

Good questions address naming, Python syntax, imports, slicing, mutation, return values, mathematical reasoning, complexity, or why a tempting alternative fails. Merge overlapping questions.

## Conclusion

Use a simple heading such as `## 정리하며`. Summarize:

- syntax or concepts made concrete;
- how the problem-solving approach changed;
- the next study direction, only if the user supplied or requested one.

## Voice

- Use calm, candid first-person Korean: `처음에는`, `정리해보니`, `다시 상기했다`.
- Prefer specific observations over dramatic claims.
- Explain beginner mistakes without embarrassment or condescension.
- Avoid repetitive phrases such as `핵심 아이디어는` in every paragraph; vary transitions naturally.
- Retain the user's characteristic wording where it is clear and accurate.
