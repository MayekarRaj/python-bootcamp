export function SectionHeader({ title, subtitle }) {
  return (
    <div className="mb-6 border-b border-slate-200 pb-3 dark:border-slate-800">
      <h2 className="text-2xl font-bold text-slate-900 dark:text-slate-100">
        {title}
      </h2>
      {subtitle && (
        <p className="mt-1 text-slate-600 dark:text-slate-400">{subtitle}</p>
      )}
    </div>
  )
}
