import { useMemo, useState } from 'react'
import { SectionHeader } from '../components/SectionHeader.jsx'
import { CodeBlock } from '../components/CodeBlock.jsx'
import { quickReference } from '../content/quickReference.js'

function QuickReference() {
  const [query, setQuery] = useState('')

  const sections = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return quickReference

    return quickReference
      .map((section) => {
        if (section.title.toLowerCase().includes(q)) return section

        const items = section.items.filter((item) =>
          `${item.name} ${item.description} ${item.code}`
            .toLowerCase()
            .includes(q),
        )
        return { ...section, items }
      })
      .filter((section) => section.items.length > 0)
  }, [query])

  return (
    <section>
      <SectionHeader
        title="Quick Reference"
        subtitle="A dense, searchable Python syntax cheat sheet"
      />

      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Filter... e.g. &quot;dict&quot;, &quot;except&quot;, &quot;@property&quot;"
        className="mb-6 w-full rounded-md border border-slate-300 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-green-500 dark:border-slate-700 dark:bg-slate-800 dark:text-slate-100 dark:placeholder-slate-500"
      />

      {sections.length === 0 && (
        <div className="rounded-lg border border-dashed border-slate-300 px-4 py-8 text-center dark:border-slate-700">
          <p className="text-2xl">🔍</p>
          <p className="mt-2 text-slate-600 dark:text-slate-400">
            Nothing found for "{query}" — try a shorter keyword.
          </p>
        </div>
      )}

      <div className="space-y-8">
        {sections.map((section) => (
          <div key={section.id}>
            <h3 className="mb-3 border-b border-slate-200 pb-2 text-lg font-bold text-slate-900 dark:border-slate-700 dark:text-slate-100">
              {section.title}
            </h3>
            <div className="grid gap-3 sm:grid-cols-2">
              {section.items.map((item) => (
                <div
                  key={item.name}
                  className="rounded-lg border border-slate-200 p-3 dark:border-slate-700"
                >
                  <p className="font-semibold text-slate-900 dark:text-slate-100">
                    {item.name}
                  </p>
                  <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
                    {item.description}
                  </p>
                  <div className="mt-2">
                    <CodeBlock code={item.code} />
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default QuickReference
