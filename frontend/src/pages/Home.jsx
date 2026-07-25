import { useState } from "react";

import Navbar from "../components/Navbar";
import PromptBox from "../components/PromptBox";
import ExecutiveSummary from "../components/ExecutiveSummary";
import ConfidenceMeter from "../components/ConfidenceMeter";
import ActionList from "../components/ActionList";
import StrategyCard from "../components/StrategyCard";
import RiskCard from "../components/RiskCard";
import ImpactCard from "../components/ImpactCard";
import ToolCard from "../components/ToolCard";
import Loading from "../components/Loading";
import Footer from "../components/Footer";

function Home() {

    const [loading] = useState(false);

    // Temporary mock data
    const strategy = {

        executive_summary:
            "Increase Product X price by 8% to maximize profit while maintaining customer retention.",

        confidence: 92,

        actions: [
            "Increase product price",
            "Notify Sales Team",
            "Update Marketing Campaign",
            "Review after 30 days"
        ],

        risks: [
            "Medium customer churn",
            "Competitor response"
        ],

        impact:
            "Expected revenue increase of 12% with minimal operational cost.",

        tools_used: [
            "Finance MCP",
            "Market MCP",
            "Legal MCP",
            "Compliance MCP"
        ]

    };

    return (

        <>

            <Navbar />

            <div className="container">

                <div className="card">

                    <h1 className="title">
                        StratOS
                    </h1>

                    <p className="subtitle">
                        Enterprise Strategy Intelligence Platform
                    </p>

                    <PromptBox />

                </div>

                {loading ? (

                    <Loading />

                ) : (

                    <>

                        <ExecutiveSummary
                            summary={strategy.executive_summary}
                        />

                        <ConfidenceMeter
                            value={strategy.confidence}
                        />

                        <StrategyCard
                            title="Overall Recommendation"
                            value="Proceed with Strategy"
                        />

                        <ImpactCard
                            impact={strategy.impact}
                        />

                        <RiskCard
                            risks={strategy.risks}
                        />

                        <ActionList
                            actions={strategy.actions}
                        />

                        <ToolCard
                            tools={strategy.tools_used}
                        />

                    </>

                )}

            </div>

            <Footer />

        </>

    );

}

export default Home;