import { CodeBlock } from './CodeBlock.jsx'

export function CheatSheetTable({ items }) {
  return (
    <div className="overflow-x-auto rounded-lg border border-slate-200">
      <table className="w-full text-left text-sm">
        <thead>
          <tr className="bg-slate-900 text-white">
            <th className="px-4 py-2 font-semibold">Concept</th>
            <th className="px-4 py-2 font-semibold">Example</th>
            <th className="px-4 py-2 font-semibold">Notes</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr
              key={item.concept}
              className={index % 2 === 0 ? 'bg-white' : 'bg-slate-50'}
            >
              <td className="px-4 py-2 align-top font-medium text-slate-900">
                {item.concept}
              </td>
              <td className="px-4 py-2 align-top">
                <CodeBlock code={item.example} />
              </td>
              <td className="px-4 py-2 align-top text-slate-600">
                {item.notes}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
