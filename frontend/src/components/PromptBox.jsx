import { useState } from "react";

function PromptBox() {

    const [prompt, setPrompt] = useState("");

    const submitPrompt = () => {

        if (prompt.trim() === "") {

            alert("Please enter a business strategy prompt.");

            return;

        }

        alert("Backend integration will be added in the next step.\n\nPrompt:\n\n" + prompt);

    };

    return (

        <div className="result-box">

            <textarea

                className="input-box"

                placeholder="Example: Increase Product X price by 10%"

                value={prompt}

                onChange={(e) => setPrompt(e.target.value)}

            />

            <br /><br />

            <button
                className="btn"
                onClick={submitPrompt}
            >

                Generate Strategy

            </button>

        </div>

    );

}

export default PromptBox;