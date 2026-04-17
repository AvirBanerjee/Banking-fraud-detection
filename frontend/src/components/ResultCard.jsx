export default function ResultCard({ result }) {
  if (!result) return null;

  const color =
    result.status === "Fraud"
      ? "bg-red-500"
      : result.status === "Suspicious"
      ? "bg-yellow-500"
      : "bg-green-500";

  return (
    <div className={`p-6 rounded-2xl shadow-lg text-white ${color}`}>
      <h2 className="text-xl font-bold">Result</h2>

      <p><b>Risk Score:</b> {result.risk_score}</p>
      <p><b>Status:</b> {result.status}</p>
      <p><b>Decision:</b> {result.decision}</p>
      <p><b>Confidence:</b> {result.confidence}</p>
      <p><b>Alert Level:</b> {result.alert_level}</p>

      <h3 className="mt-2 font-semibold">Reasons:</h3>
      <ul className="list-disc ml-5">
        {result.reasons && result.reasons.length > 0 ? (
          result.reasons.map((r, i) => <li key={i}>{r}</li>)
        ) : (
          <li>No issues detected</li>
        )}
      </ul>
    </div>
  );
}