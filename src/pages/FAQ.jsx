import { useMemo, useState } from 'react'
import { SectionHeader } from '../components/SectionHeader.jsx'
import { FAQItem } from '../components/FAQItem.jsx'
import { faqSections } from '../content/faq.js'

function FAQ() {
  const [query, setQuery] = useState('')

  const sections = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return faqSections

    return faqSections
      .map((section) => {
        const items = section.items.filter((item) =>
          `${item.question} ${item.answer}`.toLowerCase().includes(q),
        )
        return { ...section, items }
      })
      .filter((section) => section.items.length > 0)
  }, [query])

  return (
    <section>
      <SectionHeader
        title="Troubleshooting & FAQ"
        subtitle="Day 1 setup problems and common runtime errors — search or browse by category"
      />

      <div className="mb-6 rounded-lg border border-amber-300 bg-amber-50 px-4 py-3 text-sm text-amber-900 dark:border-amber-700/50 dark:bg-amber-900/20 dark:text-amber-200">
        <span className="font-semibold">Stuck?</span> Check here before
        raising your hand. Most setup problems have a fix on this page.
      </div>

      <div className="relative mb-8">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder='Search... e.g. "venv", "ModuleNotFoundError", "pip"'
          className="w-full rounded-md border border-slate-300 px-4 py-2 pr-10 text-sm focus:outline-none focus:ring-2 focus:ring-green-500 dark:border-slate-700 dark:bg-slate-800 dark:text-slate-100 dark:placeholder-slate-500"
        />
        {query && (
          <button
            type="button"
            onClick={() => setQuery('')}
            aria-label="Clear search"
            className="absolute right-2 top-1/2 -translate-y-1/2 rounded p-1 text-slate-400 transition-colors hover:text-slate-600 dark:hover:text-slate-200"
          >
            <svg
              className="h-4 w-4"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        )}
      </div>

      {sections.length === 0 && (
        <p className="text-slate-500 dark:text-slate-400">
          No results for "{query}".
        </p>
      )}

      <div className="space-y-8">
        {sections.map((section) => (
          <div key={section.id}>
            <h3 className="mb-3 flex items-center gap-2 border-b border-slate-200 pb-2 text-lg font-bold text-slate-900 dark:border-slate-700 dark:text-slate-100">
              <span className="text-xl">{section.icon}</span>
              {section.title}
            </h3>
            <div className="space-y-2">
              {section.items.map((item) => (
                <FAQItem
                  key={item.question}
                  question={item.question}
                  answer={item.answer}
                />
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default FAQ
