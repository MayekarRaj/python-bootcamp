import { SectionHeader } from '../components/SectionHeader.jsx'
import { SessionCard } from '../components/SessionCard.jsx'
import { module2 } from '../content/module2.js'

function Module2() {
  return (
    <section>
      <SectionHeader title={module2.title} subtitle={module2.subtitle} />
      <div className="space-y-4">
        {module2.sessions.map((session) => (
          <SessionCard key={session.sessionNumber} {...session} />
        ))}
      </div>
    </section>
  )
}

export default Module2
