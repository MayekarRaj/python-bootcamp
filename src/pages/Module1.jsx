import { SectionHeader } from '../components/SectionHeader.jsx'
import { SessionCard } from '../components/SessionCard.jsx'
import { module1 } from '../content/module1.js'

function Module1() {
  return (
    <section>
      <SectionHeader title={module1.title} subtitle={module1.subtitle} />
      <div className="space-y-4">
        {module1.sessions.map((session) => (
          <SessionCard key={session.sessionNumber} {...session} />
        ))}
      </div>
    </section>
  )
}

export default Module1
