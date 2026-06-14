export function ThemeToggle({ theme, onToggle }) {
  const isDark = theme === 'dark'

  return (
    <button
      type="button"
      onClick={onToggle}
      aria-label={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
      className="flex-shrink-0 rounded-md border border-slate-700 p-2 text-slate-300 transition-colors hover:border-slate-500 hover:text-white"
    >
      {isDark ? (
        <svg className="h-4 w-4" fill="currentColor" viewBox="0 0 20 20">
          <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4.22 2.78a1 1 0 011.42 1.42l-.71.7a1 1 0 11-1.41-1.41l.7-.71zM17 9a1 1 0 110 2h-1a1 1 0 110-2h1zm-7 7a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zm-5.66-1.34a1 1 0 011.41 0l.71.7a1 1 0 11-1.42 1.42l-.7-.71a1 1 0 010-1.41zM4 9a1 1 0 110 2H3a1 1 0 110-2h1zm1.34-5.66a1 1 0 010 1.41l-.7.71A1 1 0 113.22 4.04l.71-.7a1 1 0 011.41 0zM10 6a4 4 0 100 8 4 4 0 000-8z" />
        </svg>
      ) : (
        <svg className="h-4 w-4" fill="currentColor" viewBox="0 0 20 20">
          <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
        </svg>
      )}
    </button>
  )
}
