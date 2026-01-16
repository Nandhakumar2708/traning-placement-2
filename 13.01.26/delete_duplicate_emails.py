def delete_duplicate_emails(person: pd.DataFrame):
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)
