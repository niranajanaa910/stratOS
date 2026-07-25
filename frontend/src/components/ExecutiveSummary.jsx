function ExecutiveSummary({ summary }) {
  return (
    <div className="card">
      <h2 className="section-title">📄 Executive Summary</h2>

      <p className="summary-text">
        {summary || "No strategy generated yet."}
      </p>
    </div>
  );
}

export default ExecutiveSummary;