from langchain_text_splitters import RecursiveCharacterTextSplitter

text = ''' Life rarely unfolds in grand gestures alone. More often, it is shaped by the quiet rhythm of ordinary days—the small choices, the subtle acts of kindness, the unnoticed victories that accumulate over time. We tend to look for meaning in milestones: graduations, promotions, weddings, or achievements that can be neatly framed and celebrated. Yet the deeper truth is that our character is forged in the spaces between those events, in the way we carry ourselves through the mundane and the uncertain.
Consider the morning routine of someone rising early to prepare for work. The alarm rings, the body resists, but the mind insists. In that moment, discipline triumphs over comfort. It is not a headline-worthy act, but it is a victory nonetheless. Each repetition of this choice strengthens resilience, teaching us that progress is not always dramatic—it is often incremental, built brick by brick, day after day.'''

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)