import streamlit as st
from signal_proc.synthesizer import Synthesizer
import argparse

@st.cache
def synthesize(text):
    return synthesizer.synthesize(text)

def main(args):
    st.set_page_config(**PAGE_CONFIG)

    _, col2, _ = st.columns(3)
    with col2:
        st.image("assets/TPHlogo.png")

    st.header("End-to-end Burmese Speech Synthesis")
    st.write("You can type any Burmese sentences in Unicode and the model will try to synthesize the speech based on your inputs.")

    input_text = st.text_input('Input Text', placeholder="Type here")
    
    container = st.container()
    error_placeholder = st.empty()

    if st.button('Synthesize'):
        if input_text == '':
            error_placeholder.error("Input text field must be filled!")
        else:
            error_placeholder.empty()
            col4, col5 = container.columns(2)

            with col4:
                st.markdown("#### Input Text")
                st.write(input_text)

            with col5:
                st.markdown("#### Output Audio")
                
                with st.spinner('Synthesizing...'):
                    audio_placeholder = st.empty()
                    data = synthesize(input_text)

                    audio_placeholder.audio(data, format="audio/wav")   
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint', required=False, help='Full path to model checkpoint')
    args = parser.parse_args()

    synthesizer = Synthesizer()
    synthesizer.init(args.checkpoint)
    
    PAGE_CONFIG = {"page_title":"Burmese TTS - Thate Pan Hub","page_icon":"assets/TPH_Icon.png","layout":"centered"}
    
    main(args)
