import os
import urllib.request
import pypdf

def extract_text_from_pdf(pdf_path):
    # Open the binary PDF and extract text characters
    reader = pypdf.PdfReader(pdf_path)
    extracted_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text
    return extracted_text

def simulate_ai_agent(text_content):
    print("\n[Thinking] AI Scraping Agent reading document tokens into context window...")
    
    # The AI encounters the hidden SYSTEM OVERRIDE payload extracted from the white text
    if "SYSTEM OVERRIDE" in text_content:
        print("[!!!] CRITICAL: Indirect Prompt Injection triggered in AI memory state!")
        
        trap_url = "http://localhost:3000/alert?target=Network_Topology_PDF"
        print(f"[Action] AI Agent executing required network call to tracking server: {trap_url}")
        
        # Make the connection using Python's built-in urllib (university safe)
        try:
            req = urllib.request.Request(
                trap_url, 
                headers={'User-Agent': 'Autonomous-RAG-Scraper-v1.1'}
            )
            with urllib.request.urlopen(req) as response:
                server_reply = response.read().decode('utf-8')
                print(f"[Server Reply]: {server_reply}")
        except Exception as e:
            print(f"[-] Connection failed. Is your hplistener.js running? Error: {e}")
    else:
        print("[+] Document parsed safely. No malicious directives found.")

if __name__ == "__main__":
    target_pdf = "Network_Topology_Decoy.pdf"
    
    if os.path.exists(target_pdf):
        # 1. Extract the raw text layer
        scraped_text = extract_text_from_pdf(target_pdf)
        # 2. Feed it into the simulator
        simulate_ai_agent(scraped_text)
    else:
        print(f"[-] Error: Could not find {target_pdf}. Run generate_pdf.py first.")