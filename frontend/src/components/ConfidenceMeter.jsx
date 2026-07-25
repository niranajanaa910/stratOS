function ConfidenceMeter({ value }) {

  const confidence = value || 0;

  return (
    <div className="card">

      <h2 className="section-title">
        📊 Confidence
      </h2>

      <div
        style={{
          width: "100%",
          background: "#e5e7eb",
          borderRadius: "8px",
          height: "18px",
          marginTop: "15px"
        }}
      >

        <div
          style={{
            width: `${confidence}%`,
            background: "#2563eb",
            height: "100%",
            borderRadius: "8px"
          }}
        />

      </div>

      <h3 style={{marginTop:"15px"}}>
        {confidence}%
      </h3>

    </div>
  );

}

export default ConfidenceMeter;