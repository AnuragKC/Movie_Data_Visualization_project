# Movie_Data_Visualization_project

Overview:

This project is a comprehensive exploration of movie data using the TMDb API and PostgreSQL. It focuses on fetching, storing, and visualizing movie-related insights such as revenue trends and average ratings over time. The goal is to demonstrate data engineering skills through a practical, hands-on project that combines API integration, database management, and data visualization.

Features:
- API Integration: Extracts data from The Movie Database (TMDb) API.
- Database Management: Stores movie data in a PostgreSQL database for efficient querying.
- Data Analysis: Processes and cleans the data for meaningful insights.
- Visualization: Creates interactive charts to explore trends in movie revenue and average ratings.

Technologies Used:
- Python: For data extraction, processing, and visualization.
- PostgreSQL: As the database for structured data storage.
- Plotly: For creating interactive and visually appealing data visualizations.
- TMDb API: To fetch up-to-date movie data.

Steps Undertaken:
1. **API Setup**: Registered for the TMDb API and configured authentication to fetch movie data.
2. **Database Creation**: Designed a PostgreSQL database schema to store movies, including fields like `title`, `revenue`, `release_date`, `genre_ids`, and `vote_average`.
3. **Data Extraction**: Used Python to fetch data from the TMDb API and parsed the JSON responses.
4. **Data Loading**: Inserted the cleaned and processed data into the PostgreSQL database.
5. **Data Analysis**: Queried the database to aggregate metrics such as total revenue by year and average ratings.
6. **Visualization**: Used Plotly to create interactive line charts showcasing revenue trends and average ratings over time.
7. **Testing and Debugging**: Validated the data pipeline to ensure accuracy and fixed any issues.

Goals:
1. Showcase the integration of multiple technologies in a data pipeline.
2. Provide insights into movie trends, helping understand industry dynamics.
3. Serve as a portfolio project to demonstrate data engineering and visualization skills.

Project Highlights:
- Data Pipeline: Automates the process of fetching data, storing it in a database, and preparing it for analysis.
- Interactive Visualizations: Enables users to explore movie data trends dynamically.
- Scalability: Designed to accommodate additional data points and features in the future.

Future Enhancements:
- Include additional data fields like director, cast, and runtime for deeper insights.
- Expand visualization options, such as genre-specific trends and correlation heatmaps.
- Automate the data refresh process for real-time analysis.

Acknowledgements:
- TMDb API: For providing a rich dataset of movie information.
- PostgreSQL: For robust database management capabilities.
- Plotly: For powerful and intuitive visualization tools.

  Also, pycharm was used to write all the necessay python codes, it was convenient to install
  all necessary packages required for the project.

This project is for personal use and showcase only.

