import { useState } from 'react'

const KEYWORDS = new Set([
  'def', 'class', 'if', 'elif', 'else', 'for', 'while', 'return', 'import',
  'from', 'as', 'in', 'is', 'not', 'and', 'or', 'lambda', 'try', 'except',
  'finally', 'with', 'yield', 'raise', 'pass', 'break', 'continue', 'global',
  'nonlocal', 'assert', 'del', 'async', 'await',
])

const CONSTANTS = new Set(['True', 'False', 'None', 'self'])

// Matches, in priority order: comments, strings (with optional f/r prefix),
// numbers, decorators, and identifiers/keywords.
const TOKEN_REGEX =
  /(#.*)|([rRfFbB]?(?:"""[\s\S]*?"""|'''[\s\S]*?'''|"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*'))|(\b\d+(?:\.\d+)?\b)|(@[A-Za-z_]\w*)|(\b[A-Za-z_]\w*\b)/g

function highlightPython(code) {
  const nodes = []
  let lastIndex = 0
  let match
  let key = 0

  while ((match = TOKEN_REGEX.exec(code))) {
    if (match.index > lastIndex) {
      nodes.push(code.slice(lastIndex, match.index))
    }

    const [full, comment, string, number, decorator, word] = match

    if (comment) {
      nodes.push(
        <span key={key++} className="text-slate-500 italic">
          {comment}
        </span>,
      )
    } else if (string) {
      nodes.push(
        <span key={key++} className="text-emerald-400">
          {string}
        </span>,
      )
    } else if (number) {
      nodes.push(
        <span key={key++} className="text-orange-400">
          {number}
        </span>,
      )
    } else if (decorator) {
      nodes.push(
        <span key={key++} className="text-cyan-400">
          {decorator}
        </span>,
      )
    } else if (word) {
      const nextChar = code[match.index + full.length]
      if (KEYWORDS.has(word)) {
        nodes.push(
          <span key={key++} className="text-purple-400">
            {word}
          </span>,
        )
      } else if (CONSTANTS.has(word)) {
        nodes.push(
          <span key={key++} className="text-sky-400">
            {word}
          </span>,
        )
      } else if (nextChar === '(') {
        nodes.push(
          <span key={key++} className="text-yellow-300">
            {word}
          </span>,
        )
      } else {
        nodes.push(word)
      }
    }

    lastIndex = match.index + full.length
  }

  if (lastIndex < code.length) {
    nodes.push(code.slice(lastIndex))
  }

  return nodes
}

export function CodeBlock({ code }) {
  const [copied, setCopied] = useState(false)

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code)
      setCopied(true)
      setTimeout(() => setCopied(false), 1500)
    } catch {
      setCopied(false)
    }
  }

  return (
    <div className="relative">
      <pre className="overflow-x-auto rounded-md bg-slate-900 px-3 py-2 pr-14 text-xs leading-relaxed text-slate-100">
        <code className="font-mono">{highlightPython(code)}</code>
      </pre>
      <button
        type="button"
        onClick={handleCopy}
        className="absolute right-2 top-2 rounded bg-slate-700 px-2 py-1 text-xs font-medium text-slate-200 transition-colors hover:bg-slate-600"
      >
        {copied ? 'Copied!' : 'Copy'}
      </button>
    </div>
  )
}
