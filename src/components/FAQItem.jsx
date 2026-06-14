import { useState } from 'react'

export function FAQItem({ question, answer }) {
  const [expanded, setExpanded] = useState(false)

  return (
    <div
      className={`overflow-hidden rounded-lg border bg-white transition-colors dark:bg-slate-800 ${
        expanded
          ? 'border-green-300 dark:border-green-700'
          : 'border-slate-200 dark:border-slate-700'
      }`}
    >
      <button
        type="button"
        onClick={() => setExpanded((prev) => !prev)}
        aria-expanded={expanded}
        className="flex w-full items-center justify-between gap-3 px-4 py-3 text-left transition-colors hover:bg-slate-50 dark:hover:bg-slate-700/50"
      >
        <span className="font-semibold text-slate-900 dark:text-slate-100">
          {question}
        </span>
        <svg
          className={`h-5 w-5 flex-shrink-0 text-slate-400 transition-transform dark:text-slate-500 ${
            expanded ? 'rotate-180' : ''
          }`}
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      <div
        className={`grid overflow-hidden transition-all duration-300 ease-in-out ${
          expanded ? 'grid-rows-[1fr] opacity-100' : 'grid-rows-[0fr] opacity-0'
        }`}
      >
        <div className="min-h-0 overflow-hidden">
          <p className="whitespace-pre-line border-l-4 border-green-400 bg-green-50 px-4 py-3 text-sm leading-relaxed text-slate-700 dark:border-green-600 dark:bg-green-900/20 dark:text-slate-300">
            {answer}
          </p>
        </div>
      </div>
    </div>
  )
}
