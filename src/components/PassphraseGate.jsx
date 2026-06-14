import { useState } from 'react'

const PASSPHRASE = 'python2026'
const AUTH_KEY = 'bootcamp_auth'

function PassphraseGate({ children }) {
  const [authenticated, setAuthenticated] = useState(
    () => localStorage.getItem(AUTH_KEY) === 'true',
  )
  const [input, setInput] = useState('')
  const [error, setError] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    if (input === PASSPHRASE) {
      localStorage.setItem(AUTH_KEY, 'true')
      setAuthenticated(true)
      setError(false)
    } else {
      setError(true)
    }
  }

  if (authenticated) {
    return children
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-900 px-4">
      <div className="w-full max-w-sm rounded-xl bg-slate-800 p-8 shadow-lg">
        <h1 className="text-center text-xl font-bold text-white">
          Python Bootcamp — June 2026
        </h1>
        <form onSubmit={handleSubmit} className="mt-6 space-y-3">
          <input
            type="password"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Enter passphrase"
            autoFocus
            className="w-full rounded-md border border-slate-600 bg-slate-700 px-4 py-3 text-base text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            className="w-full rounded-md bg-blue-600 px-4 py-3 text-base font-medium text-white transition-colors hover:bg-blue-700"
          >
            Submit
          </button>
          {error && (
            <p className="text-sm text-red-400">
              Incorrect passphrase. Check with your instructor.
            </p>
          )}
        </form>
      </div>
    </div>
  )
}

export default PassphraseGate
