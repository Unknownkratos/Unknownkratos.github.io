# SpartaTunes

## Overview
The "SpartaTunes" Java program is a creative application that allows users to input a series of numbers and triggers the playback of corresponding musical soundtracks. It utilizes Java's javax.sound.sampled library to load and play audio files based on the user's input.

## Code Explanation
The provided Java program comprises the following key components:

### Loading Soundtracks
The `loadSoundtracks` method initializes an array of `Clip` objects, each representing a specific musical soundtrack. It iterates through digits 0-9 and loads the corresponding audio file for each digit, if available.

### Playing Music
The `playMusic` method processes the user input and triggers the playback of the corresponding musical soundtracks. It calculates the total duration of all soundtracks to ensure that the program's thread sleeps for an appropriate duration after playing the soundtracks.

### Main Method
The main method prompts the user to input a number and then invokes the `playMusic` method to play the corresponding musical soundtracks.

## Execution
To execute the program, follow these steps:

1. Compile the Java source file using a Java compiler.
2. Ensure that the audio files (e.g., "0.wav", "1.wav", etc.) corresponding to each digit are present in the working directory.
3. Run the compiled Java program.

Upon executing the program, the user can input a series of numbers, and the program will play the corresponding musical soundtracks.

## Conclusion
The "SpartaTunes" Java program demonstrates a unique and engaging way to combine user input and audio playback. It showcases the application of sound manipulation in a Java environment and offers an interactive user experience through music.

The use of Java's sound libraries and the effective handling of audio file loading and playback underscore the program's capability to blend numerical input with auditory feedback, creating an innovative and entertaining application.

