import { Navigate, NavLink, Route, Routes } from 'react-router-dom'
import PassphraseGate from './components/PassphraseGate.jsx'
import { ThemeToggle } from './components/ThemeToggle.jsx'
import { useTheme } from './hooks/useTheme.js'
import FAQ from './pages/FAQ.jsx'
import Module1 from './pages/Module1.jsx'
import Module2 from './pages/Module2.jsx'
import Module3 from './pages/Module3.jsx'
import Module4 from './pages/Module4.jsx'
import QuickReference from './pages/QuickReference.jsx'
import WhatsNext from './pages/WhatsNext.jsx'

const tabs = [
  { to: '/module-1', label: 'Module 1 — Foundations' },
  { to: '/module-2', label: 'Module 2 — Intermediate' },
  { to: '/module-3', label: 'Module 3 — OOP' },
  { to: '/module-4', label: 'Module 4 — Data Handling' },
  { to: '/quick-reference', label: 'Quick Reference' },
  { to: '/whats-next', label: "What's Next" },
  { to: '/faq', label: '🛠 Troubleshoot' },
]

function App() {
  const { theme, toggleTheme } = useTheme()

  return (
    <PassphraseGate>
      <div className="min-h-screen bg-white text-slate-900 dark:bg-slate-950 dark:text-slate-100">
        <header className="sticky top-0 z-20 bg-slate-900 text-white shadow-md">
          <div className="mx-auto flex max-w-5xl items-center justify-between gap-3 px-4 py-3">
            <h1 className="text-lg font-bold tracking-tight">
              Python Bootcamp
            </h1>
            <div className="flex items-center gap-3">
              <span className="text-sm text-slate-300">June 15–19, 2026</span>
              <ThemeToggle theme={theme} onToggle={toggleTheme} />
            </div>
          </div>
          <nav className="border-t border-slate-700 overflow-x-auto">
            <div className="mx-auto flex max-w-5xl gap-2 px-2 py-2.5">
              {tabs.map((tab) => (
                <NavLink
                  key={tab.to}
                  to={tab.to}
                  className={({ isActive }) =>
                    `flex-shrink-0 whitespace-nowrap rounded-full px-4 py-2 text-sm font-medium transition-colors ${
                      isActive
                        ? 'bg-green-500 text-slate-900'
                        : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                    }`
                  }
                >
                  {tab.label}
                </NavLink>
              ))}
            </div>
          </nav>
        </header>

        <main className="mx-auto max-w-5xl px-4 py-8">
          <Routes>
            <Route path="/" element={<Navigate to="/module-1" replace />} />
            <Route path="/module-1" element={<Module1 />} />
            <Route path="/module-2" element={<Module2 />} />
            <Route path="/module-3" element={<Module3 />} />
            <Route path="/module-4" element={<Module4 />} />
            <Route path="/quick-reference" element={<QuickReference />} />
            <Route path="/whats-next" element={<WhatsNext />} />
            <Route path="/faq" element={<FAQ />} />
          </Routes>
        </main>

        <footer className="border-t border-slate-200 py-6 text-center text-sm text-slate-500 dark:border-slate-800 dark:text-slate-400">
          Python Bootcamp · June 15–19, 2026 · Made with ☕ and Python
        </footer>
      </div>
    </PassphraseGate>
  )
}

export default App
