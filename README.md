# Spotify Top Tracks CLI

A simple **Command Line Interface (CLI)** project that lets you search for an artist and display their **top 5 tracks** along with relevant information using the **Spotify Web API**.  

---

## Features
- Search for any artist available on Spotify.
- Display **artist information**:  
  - Name  
  - Followers  
  - Genres  
  - Popularity score
- Display **top 5 tracks** with details:  
  - Track name  
  - Album name  
  - Release date  
  - Duration  
  - Popularity  
  - Preview URL (if available)

---

## What I Learned
- How to use the **Spotify Web API** with **Client Credentials Flow**.
- Making **HTTP requests** using `requests` library in Python.
- Handling **JSON responses** and extracting relevant data.
- Formatting and presenting information cleanly in a CLI.
- Dealing with API limitations, such as inaccessible tracks or region restrictions.

---

## How it Works
1. The user inputs an **artist name**.
2. The program uses Spotify’s API to **search for the artist**.
3. Fetches the **artist’s top tracks** in the US market.
4. Prints the artist and track information in a readable format.

---

## Setup
1. Clone the repository.
2. Create a `.env` file with your Spotify API credentials:

