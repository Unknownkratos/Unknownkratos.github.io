---
title: "ScreenSurf – A Minimal Movie Recommendation Web App"
tags: [screensurf, react, typescript, movies, fullstack]
date: "2023-11-20"
author: me
language: en
---

# ScreenSurf – A Movie Recommendation Web App

## Project Overview

**ScreenSurf** is a web-based movie recommendation platform that allows users to discover movies through a simple swipe interface. Users indicate whether they like or dislike movies, and ScreenSurf builds a personalized list of suggestions based on those inputs.

The app focuses on a clean interface, smooth interaction, and consistent movie discovery experience. It supports user login, browsing by genre or rating, and maintaining a favorites list. No AI models are involved—recommendations are driven by input filtering and smart selection logic.

## Stack

- **Frontend:** React with TypeScript, functional components, and hooks  
- **Backend:** Express.js with Axios for third-party API calls (TMDB)  
- **Authentication:** Token-based user auth for login and preference storage  
- **Features:**  
  - Like/dislike movie swiping  
  - Top movie suggestions based on user taste  
  - Genre, rating, and search filters  
  - Favorites and watch history  
  - Fully responsive layout


Screenshots
===========

Login Page
----------

```{image} ../_static/img/ScreenSurf/login.png
:align: center
:width: 700
:alt: Login screen
```

Browse Page
-----------

```{image} ../_static/img/ScreenSurf/Browse.png
:align: center
:width: 700
:alt: Browsing Page
```

Home Page
---------

```{image} ../_static/img/ScreenSurf/Home.png
:align: center
:width: 700
:alt: Home Page
```
