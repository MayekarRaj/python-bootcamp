export const module4 = {
  title: 'Module 4 — Data Handling',
  subtitle: 'Sessions 9–10: NumPy, Pandas, and the capstone project',
  datasetUrl:
    'https://raw.githubusercontent.com/dsrscientist/dataset1/master/IPL_Data.csv',
  sessions: [
    {
      sessionNumber: 9,
      title: 'NumPy & Pandas + IPL Dataset',
      topics: [
        'NumPy arrays basics',
        'Pandas Series and DataFrame',
        'read_csv',
        'Filtering',
        'groupby',
        'sort_values',
        'Data cleaning',
      ],
      cheatsheet: [
        {
          concept: 'Read CSV',
          description: 'import pandas as pd; df = pd.read_csv("ipl.csv")',
        },
        {
          concept: 'Inspect',
          description: 'df.head(), df.shape, df.columns, df.info(), df.describe()',
        },
        {
          concept: 'Filter',
          description: 'df[df["runs"] > 50] or df.query("runs > 50")',
        },
        {
          concept: 'GroupBy',
          description: 'df.groupby("team")["runs"].sum().reset_index()',
        },
        {
          concept: 'Sort',
          description:
            'df.sort_values("strike_rate", ascending=False).head(10)',
        },
        {
          concept: 'Data cleaning',
          description: 'df.dropna(), df.fillna(0), df["col"].astype(int)',
        },
        {
          concept: 'New column',
          description:
            'df["strike_rate"] = (df["runs"] / df["balls"]) * 100',
        },
      ],
      problem:
        'From the IPL dataset, find the top 5 batsmen by total runs who have faced at least 200 balls. Display their name, total runs, and calculated strike rate.',
      takehome:
        'Find which IPL team has the highest average run rate across all matches they batted in. Show your working with groupby.',
    },
    {
      sessionNumber: 10,
      title: 'Capstone + Wrap-up',
      topics: ['Project presentations', 'Code walkthrough', 'Peer review'],
      cheatsheet: [],
      problem:
        "Present your mini project. Walk through: what it does, how you structured it, one thing you'd improve.",
      takehome:
        'Push your final project to GitHub with a README that explains what the project does, how to run it, and what you learned.',
    },
  ],
}
