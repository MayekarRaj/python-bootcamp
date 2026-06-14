import { useState } from 'react'

export function SessionCard({
  sessionNumber,
  title,
  topics,
  cheatsheet,
  problem,
  takehome,
}) {
  const [expanded, setExpanded] = useState(false)

  return (
    <div className="overflow-hidden rounded-lg border border-slate-200 bg-white shadow-sm dark:border-slate-700 dark:bg-slate-800">
      <button
        type="button"
        onClick={() => setExpanded((prev) => !prev)}
        aria-expanded={expanded}
        className="flex w-full items-center justify-between gap-4 px-4 py-3 text-left transition-colors hover:bg-slate-50 dark:hover:bg-slate-700/50"
      >
        <div className="flex items-center gap-3">
          <span className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-slate-900 text-sm font-bold text-white dark:bg-slate-700">
            {sessionNumber}
          </span>
          <span className="font-semibold text-slate-900 dark:text-slate-100">
            {title}
          </span>
        </div>
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
        <div className="min-h-0 space-y-6 overflow-hidden border-t border-slate-100 px-4 py-5 dark:border-slate-700">
          <section>
            <h3 className="mb-2 text-sm font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
              Topics Covered
            </h3>
            <ul className="flex flex-wrap gap-2">
              {topics.map((topic) => (
                <li
                  key={topic}
                  className="rounded-full bg-green-50 px-3 py-1 text-sm font-medium text-green-700 dark:bg-green-900/40 dark:text-green-300"
                >
                  {topic}
                </li>
              ))}
            </ul>
          </section>

          {cheatsheet && cheatsheet.length > 0 && (
            <section>
              <h3 className="mb-2 text-sm font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
                Cheat Sheet
              </h3>
              <div className="overflow-x-auto rounded-lg border border-slate-200 dark:border-slate-700">
                <table className="w-full text-left text-sm">
                  <thead>
                    <tr className="bg-slate-900 text-white">
                      <th className="px-4 py-3 font-semibold">Concept</th>
                      <th className="px-4 py-3 font-semibold">Description</th>
                    </tr>
                  </thead>
                  <tbody>
                    {cheatsheet.map((item, index) => (
                      <tr
                        key={item.concept}
                        className={
                          index % 2 === 0
                            ? 'bg-white dark:bg-slate-800'
                            : 'bg-slate-50 dark:bg-slate-800/60'
                        }
                      >
                        <td className="px-4 py-3 align-top font-medium leading-relaxed text-slate-900 dark:text-slate-100">
                          {item.concept}
                        </td>
                        <td className="px-4 py-3 align-top leading-relaxed text-slate-600 dark:text-slate-400">
                          {item.description}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>
          )}

          <section>
            <h3 className="mb-2 text-sm font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
              Problem of the Session
            </h3>
            <div className="rounded-lg border-l-4 border-green-500 bg-green-50 px-4 py-3 text-slate-800 dark:bg-green-900/20 dark:text-slate-100">
              {problem}
            </div>
          </section>

          <section>
            <h3 className="mb-2 text-sm font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
              Take-Home Problem
            </h3>
            <p className="text-slate-700 dark:text-slate-300">{takehome}</p>
          </section>
        </div>
      </div>
    </div>
  )
}
