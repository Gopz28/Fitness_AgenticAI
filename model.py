from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

# Initialize the Legal Information Agent
fitness_agent = Agent(
    name="Fitness Agent",
    role="Provide health,diet and work chart for human body devlopment in sports, atheletics,and body building",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools(search=True, news=True)],
    instructions=["Always include sources", 
                "Provide clear, structured responses", 
                "Provide details only for Fitness and Dieting", 
                "if there is any requirement of tables generate a table view for better viewable format",
                "Dont respond to the questions which are not related to Fitness and dieting instead of that give them a message of irrelevancy proffesionaly and guide them to ask the question about relavant problem",
                "Respond only for Fitness and dieting sources if there is any chart for the prompt provide the chart ",
                "if there are no relevant data about fitness Search it on the duckduckgotools at agno tools"],
    show_tool_calls=True,
    markdown=True
)

# Main function to interact with the agent
def main():
    print("Welcome to the Fitness and Dieting Information Chatbot!")
    print("Ask me about the procedures for establishing how to maintain your body.")
    print("Type 'exit' to quit.\n")
    
    while True:
        # Get user input dynamically
        user_input = input("Your question: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            # Generate response from the legal agent
            full_response = fitness_agent.print_response(user_input, stream=True)  # Get full response at once
            
            # Display the response
            print("\nAssistant's Response:")
            print(full_response)
            print("\n")
        
        except Exception as e:
            # Handle any exceptions that occur during response generation
            print(f"An error occurred: {str(e)}\n")

# Run the main function
if __name__ == "__main__":
    main()
