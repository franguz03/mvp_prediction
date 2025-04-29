# mvp_prediction
End-to-end project to make predictions about how likely a player is to win the NBA MVP

## Overview
End-to-end project to make predictions about how likely a player is to win the NBA MVP. The process follows a structured development approach consisting of multiple phases:

1. Scraping
2. Data cleaning
3. Exploratory Data Analysis
4. Modeling
5. Deployment

## Technologies Used
- skelearn
- Tensorflow
- Scikeras
- Pandas
- Flask
- Matplotlib
- Seaborn
- Docker
- BeautifulSoup

## Dataset
The main dataset contains the next features:
- **Player**: Player's full name.
- **Age**: Player's age.
- **Abbreviation**: Team abbreviation.
- **Pos**: Position (PG, SG, SF, PF, C).
- **G**: Games played.
- **GS**: Games started.
- **MP**: Minutes played.
- **FG**: Field goals made.
- **FGA**: Field goals attempted.
- **FG%**: Field goal percentage.
- **3P**: Three-point field goals made.
- **3PA**: Three-point field goals attempted.
- **3P%**: Three-point percentage.
- **2P**: Two-point field goals made.
- **2PA**: Two-point field goals attempted.
- **2P%**: Two-point percentage.
- **eFG%**: Effective field goal percentage (accounts for 3-point shots).
- **FT**: Free throws made.
- **FTA**: Free throws attempted.
- **FT%**: Free throw percentage.
- **ORB**: Offensive rebounds.
- **DRB**: Defensive rebounds.
- **TRB**: Total rebounds.
- **AST**: Assists.
- **STL**: Steals.
- **BLK**: Blocks.
- **TOV**: Turnovers.
- **PF**: Personal fouls.
- **PTS**: Total points scored.
- **Awards**: Awards received (e.g., MVP).
- **Year**: Season year.
- **voting_first**: First-place votes in MVP voting.
- **voting_pts_won**: Total points received in MVP voting.
- **voting_pts_max**: Maximum possible voting points.
- **voting_share**: Share of voting points (points won / points max).
- **advanced_ws**: Win Shares (estimated number of wins contributed by player).
- **advanced_ws_per_48**: Win Shares per 48 minutes.
- **Team**: Team name.
- **W**: Team wins.
- **L**: Team losses.
- **W/L%**: Team win percentage.
- **GB**: Games behind the conference/division leader.
- **PS/G**: Team points scored per game.
- **PA/G**: Team points allowed per game.
- **SRS**: Simple Rating System (point differential adjusted for strength of schedule).

## Scraping

Data was scraped from **Basketball Reference** using `requests` and `BeautifulSoup`. The dataset includes advanced and per-game stats for NBA players, team stats, and MVP voting data from past seasons. Key endpoints:

- Player stats per season
- Team stats per season
- MVP voting results per season

The data was saved in CSV format for further processing.

## Data Cleaning & Feature Engineering

## Data Cleaning & Feature Engineering

### 1. Resolving Players Who Played for Multiple Teams in the Same Season
  Players who played for more than one team within the same season had their stats correctly assigned to each team, ensuring accurate performance tracking.
  
### 2. Merging Player Stats with MVP Candidates Stats
  All player statistics were merged with MVP candidate stats to create a unified dataset for analysis, ensuring no information was missed for relevant players.

### 3. Handling Missing Data for Non-Candidate Players
  We filled missing data for players not included as MVP candidates, ensuring the dataset remained complete and consistent.

### 4. Resolving Team Data Issues
  Inconsistencies and missing values in the team data were resolved, ensuring all team-related information was accurate and up-to-date.

### 5. Merging Team Stats with Player Stats
  Team statistics were integrated with individual player stats, allowing us to correlate team performance with individual player contributions.


## Exploratory Data Analysis

### 1. Average MVP Candidates' Stats Over the Years
  This analysis tracks the evolution of key statistics (points, assists, rebounds) for MVP candidates. It shows a significant increase in points over recent years.
  - **Chart:** `lineplot` displaying the yearly trend of MVP candidates' statistics.

### 2. Best Scores with More Than 60 Games Played
  This highlights players with the highest scores in seasons where they played more than 60 games.
  - **Chart:** `barplot` showing the highest scores by season.

### 3. Correlation Between MVP Voting Share and Key Stats
  The analysis reveals a strong correlation between MVP voting share and stats like points and assists, highlighting the importance of these factors in the voting process.
  - **Chart:** `heatmap` displaying the correlation between key stats and MVP voting share.

### 4. Best Defensive Seasons Using Steals and Blocks
  This focuses on the best defensive seasons based on steals (STL) and blocks (BLK), showcasing the most defensive players.
  - **Chart:** `barplot` showing the seasons with the most steals and blocks.




## Model Building

### 1. Base Model Definition (Ridge Regression)
  A base model was created using Ridge Regression to provide a benchmark for the analysis.

### 2. Evaluation Metrics Development
  Several evaluation metrics were explored, with a custom metric designed based on cumulative precision to better evaluate the model's performance.

### 3. Backtesting with Temporal Sequence Preservation
  A backtesting strategy was defined that respects the temporal sequence of the records, ensuring the evaluation process aligns with the time-based nature of the data.

### 4. Proposed Models
  Multiple models were proposed for testing, including:
  - Ridge Regression
  - Lasso Regression
  - Linear Regression
  - Support Vector Regression (SVR)
  - Random Forest
  - Different neural network architectures using TensorFlow



### Model Performance

	model	mean_ap	std_ap
	ridge_regression	0.734793	0.168011
	lasso_regression	0.219314	0.035886
	linear_regression	0.728973	0.174458
	svr	0.794756	0.167586
	random_forest	0.740563	0.148961
	nn	0.728139	0.201166

## Model Deployment

The MVP prediction model was deployed using **Flask** as the web framework and containerized using **Docker**.

The Flask app serves a web interface where users can input player statistics and receive a prediction on their MVP chances. This allows for easy integration into other systems or frontend applications via API.

A `Dockerfile` was created to encapsulate the app and its dependencies, ensuring portability and ease of deployment.

### Running with Docker

```bash
# Clone the repository
git clone https://github.com/franguz03/mvp_prediction.git
cd mvp_prediction

# Build the Docker image
docker build -t mvp-prediction .

# Run the container
docker run -p 5000:5000 mvp-prediction
```

## Future Improvements
- Improving the Neuronal networks performance.
- perform hyperparameter optimization on the models.


## Author
Franco José Guzmán Orjuela
francorjuela04@gmail.com




