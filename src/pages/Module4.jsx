import { SectionHeader } from '../components/SectionHeader.jsx'
import { SessionCard } from '../components/SessionCard.jsx'
import { module4 } from '../content/module4.js'

function Module4() {
  const [session9, session10] = module4.sessions

  return (
    <section>
      <SectionHeader title={module4.title} subtitle={module4.subtitle} />

      <div className="mb-4 flex flex-col items-start justify-between gap-3 rounded-lg border border-green-200 bg-green-50 px-4 py-3 sm:flex-row sm:items-center dark:border-green-800 dark:bg-green-900/20">
        <div>
          <p className="font-semibold text-slate-900 dark:text-slate-100">
            IPL Dataset
          </p>
          <p className="text-sm text-slate-600 dark:text-slate-400">
            Used in Session 9 for the NumPy &amp; Pandas exercises.
          </p>
        </div>
        <a
          href={module4.datasetUrl}
          download
          target="_blank"
          rel="noreferrer"
          className="flex-shrink-0 rounded-md bg-green-600 px-4 py-2 text-sm font-semibold text-white transition-colors hover:bg-green-700"
        >
          Download CSV
        </a>
      </div>

      <div className="space-y-4">
        <SessionCard {...session9} />
      </div>

      <div className="mt-8 rounded-lg border border-green-300 bg-gradient-to-r from-green-50 via-emerald-50 to-green-50 px-4 py-4 text-center dark:border-green-700 dark:from-green-900/30 dark:via-emerald-900/30 dark:to-green-900/30">
        <p className="text-lg font-bold text-green-700 dark:text-green-400">
          🎉 You made it — Capstone Day!
        </p>
        <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
          Time to show off everything you've built this week. Great work!
        </p>
      </div>

      <div className="mt-3 rounded-lg ring-2 ring-green-400 dark:ring-green-600">
        <SessionCard {...session10} />
      </div>
    </section>
  )
}

export default Module4
