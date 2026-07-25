import { API_URL } from "../utils/constants";

export async function generateStrategy(prompt) {

  try {

    const response = await fetch(API_URL, {

      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        prompt: prompt
      })

    });

    return await response.json();

  } catch (error) {

    console.error(error);

    return {
      executive_summary: "Unable to connect to backend.",
      confidence: 0,
      actions: [],
      risks: [],
      impact: "",
      tools_used: []
    };

  }

}