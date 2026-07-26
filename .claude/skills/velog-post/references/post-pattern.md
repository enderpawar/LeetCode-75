# Post Pattern

Use this pattern as a flexible house style. Omit empty subsections instead of forcing content.

## Title

Use this form when appropriate:

```text
[알고리즘 스터디 N주차] 학습 주제를 드러내는 제목
```

Name the shared concept rather than listing problem titles only.

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
```

Explain the code in execution order. State why boundary cases work. Do not repeat every line mechanically.

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
