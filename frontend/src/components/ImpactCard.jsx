function ImpactCard({ impact }) {

  return (

    <div className="card">

      <h2 className="section-title">
        📈 Business Impact
      </h2>

      <p>
        {impact || "No impact analysis available."}
      </p>

    </div>

  );

}

export default ImpactCard;