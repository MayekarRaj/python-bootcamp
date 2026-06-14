import { SectionHeader } from '../components/SectionHeader.jsx'
import { whatsNext } from '../content/whatsNext.js'

function WhatsNext() {
  return (
    <section>
      <SectionHeader title={whatsNext.title} subtitle={whatsNext.subtitle} />

      <div className="space-y-10">
        <div>
          <h3 className="mb-3 text-lg font-bold text-slate-900 dark:text-slate-100">
            Practice Platforms
          </h3>
          <div className="grid gap-3 sm:grid-cols-3">
            {whatsNext.practicePlatforms.map((platform) => (
              <a
                key={platform.name}
                href={platform.url}
                target="_blank"
                rel="noreferrer"
                className="rounded-lg border border-slate-200 p-4 transition-colors hover:border-green-300 hover:bg-green-50 dark:border-slate-700 dark:hover:border-green-700 dark:hover:bg-green-900/20"
              >
                <div className="text-2xl">{platform.icon}</div>
                <p className="mt-2 font-semibold text-slate-900 dark:text-slate-100">
                  {platform.name}
                </p>
                <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
                  {platform.description}
                </p>
              </a>
            ))}
          </div>
        </div>

        <div>
          <h3 className="mb-3 text-lg font-bold text-slate-900 dark:text-slate-100">
            Projects to Build
          </h3>
          <div className="grid gap-3 sm:grid-cols-2">
            {whatsNext.projects.map((project) => (
              <div
                key={project.title}
                className="rounded-lg border border-slate-200 p-4 dark:border-slate-700"
              >
                <div className="text-2xl">{project.icon}</div>
                <p className="mt-2 font-semibold text-slate-900 dark:text-slate-100">
                  {project.title}
                </p>
                <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
                  {project.description}
                </p>
              </div>
            ))}
          </div>
        </div>

        <div>
          <h3 className="mb-3 text-lg font-bold text-slate-900 dark:text-slate-100">
            What to Learn Next
          </h3>
          <ol className="space-y-3">
            {whatsNext.learnNext.map((step, index) => (
              <li
                key={step.title}
                className="flex gap-4 rounded-lg border border-slate-200 p-4 dark:border-slate-700"
              >
                <div className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-slate-900 text-sm font-bold text-white dark:bg-slate-700">
                  {index + 1}
                </div>
                <div>
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-xl">{step.icon}</span>
                    <p className="font-semibold text-slate-900 dark:text-slate-100">
                      {step.title}
                    </p>
                    <span className="rounded-full bg-green-50 px-2 py-0.5 text-xs font-medium text-green-700 dark:bg-green-900/40 dark:text-green-300">
                      {step.timeframe}
                    </span>
                  </div>
                  <p className="mt-1 text-sm text-slate-600 dark:text-slate-400">
                    {step.description}
                  </p>
                </div>
              </li>
            ))}
          </ol>
        </div>

        <div>
          <h3 className="mb-3 text-lg font-bold text-slate-900 dark:text-slate-100">
            Your GitHub Profile
          </h3>
          <ul className="space-y-2">
            {whatsNext.githubProfile.map((item) => (
              <li
                key={item.text}
                className="flex items-start gap-3 rounded-lg border border-slate-200 p-3 dark:border-slate-700"
              >
                <span className="text-xl">{item.icon}</span>
                <span className="text-slate-700 dark:text-slate-300">
                  {item.text}
                </span>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h3 className="mb-3 text-lg font-bold text-slate-900 dark:text-slate-100">
            Resources
          </h3>
          <div className="grid gap-3 sm:grid-cols-2">
            {whatsNext.resources.map((resource) => (
              <a
                key={resource.name}
                href={resource.url}
                target="_blank"
                rel="noreferrer"
                className="flex items-center gap-3 rounded-lg border border-slate-200 p-3 transition-colors hover:border-green-300 hover:bg-green-50 dark:border-slate-700 dark:hover:border-green-700 dark:hover:bg-green-900/20"
              >
                <span className="text-xl">{resource.icon}</span>
                <span className="font-medium text-slate-900 dark:text-slate-100">
                  {resource.name}
                </span>
              </a>
            ))}
          </div>
        </div>

        <div className="rounded-lg border-l-4 border-green-500 bg-green-50 px-5 py-4 dark:bg-green-900/20">
          <p className="text-slate-800 dark:text-slate-100">
            {whatsNext.closingNote.text}
          </p>
          <p className="mt-2 text-sm font-medium text-green-700 dark:text-green-400">
            {whatsNext.closingNote.attribution}
          </p>
        </div>
      </div>
    </section>
  )
}

export default WhatsNext
