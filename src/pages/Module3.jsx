import { SectionHeader } from '../components/SectionHeader.jsx'
import { SessionCard } from '../components/SessionCard.jsx'
import { module3 } from '../content/module3.js'

function Module3() {
  return (
    <section>
      <SectionHeader title={module3.title} subtitle={module3.subtitle} />
      <div className="space-y-4">
        {module3.sessions.map((session) => (
          <SessionCard key={session.sessionNumber} {...session} />
        ))}
      </div>
    </section>
  )
}

export default Module3
