function StrategyCard({ title, value }) {
  return (
    <div className="card">
      <h3 className="section-title">{title}</h3>

      <p
        style={{
          fontSize: "20px",
          fontWeight: "bold",
          color: "#2563eb",
          marginTop: "15px",
        }}
      >
        {value}
      </p>
    </div>
  );
}

export default StrategyCard;