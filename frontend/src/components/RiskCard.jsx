function RiskCard({ risks = [] }) {
  return (
    <div className="card">

      <h2 className="section-title">
        ⚠ Risk Analysis
      </h2>

      {risks.length === 0 ? (
        <p>No risks identified.</p>
      ) : (
        <ul>
          {risks.map((risk, index) => (
            <li key={index} style={{ marginBottom: "10px" }}>
              {risk}
            </li>
          ))}
        </ul>
      )}

    </div>
  );
}

export default RiskCard;