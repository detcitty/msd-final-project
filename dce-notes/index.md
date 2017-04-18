# title: Moods and activities in music
- grant: ES/K00753X/1
- date: 16/10/2015
- authors: T. Eerola, P. Saari
- affliation: Durham University, UK
- subset: Main data
- location: UK DataService ReShare
- citation: University of Durham. Department of Music, Tagging music for emotions [computer file]. 1st Edition. Durham, Country Durham: UK Data Archive [distributor], September 2015, http://dx.doi.org/ [to be added]

## users.csv

Information about each user (2508 rows, 7 columns)
- `userid` *[integer]*: unique id for each user
- `expertise` *[string]*: musical expertise (*1 Nonmusician*,*2 Music-loving nonmusician*,*3 Amateur musician*,*4 Serious amateur musician*,*5 Semi-professional musician*,*6 Professional musician*)
- `language_skill` *[string]*: language skill (*1 No proficiency*,*2 Elementary proficiency*,*3 Limited working proficiency*,*4 Professional working proficiency*,*5 Full professional proficiency*,*6 Native or bilingual proficiency*)
- `gender` *[string]*: (male,female,other)
- `age` *[integer]*: age in years (16-79)
- `country` *[string]*: two digit country code (ISO3166-1-Alpha-2)
- `continent` *[string]*: (*Africa*,*Asia*,*Europe*,*North America*,*Oceania*,*South America*)

## tracks.csv

Information about the tracks that were submitted and included in the tasks (5129 rows, 8 columns)
- `trackid` *[integer]*: track id at 7digital.com
- `artistname` *[string]*: artist
- `tracknumber` *[integer]*: number of the track in an release
- `duration` *[integer]*: duration of the track in seconds
- `artistid` *[integer]*: artist id at 7digital.com
- `tracktitle` *[string]*: track
- `releasetitle` *[string]*: release
- `releaseid` *[integer]*: release id at 7digital.com

## activities.csv

Information about the activities (9 rows, 3 columns)
- `activity` *[string]*: activity name
- `info` *[string]*: activity examples
- `description` *[string]*: longer description

## genreclusters.csv

Genre cluster label for each genre (112 rows, 2 columns)
- `genre` *[string]*: genre name
- `cluster` *[string]*: cluster label

## bg_activities_general.csv

Answers by each user to a question: "How important are the following types of activities in your life?" (2508 rows, 10 columns)
- `userid` *[integer]*: user who submitted the answers
- `activity.daily_routines`...`activity.social` *[integer]*: value (1-5) for each activity

## bg_activities_musical.csv

Answers by each user to a question: "How important is music to you in the following types of activities?" (2508 rows, 10 columns)
- `userid` *[integer]*: user who submitted the answers
- `activity.daily_routines`...`activity.social` *[integer]*: value (1-5) for each activity

## bg_genres.csv

Answers by each user to a question: "Which musical genres do you like?" (2508 rows, 113 columns)
- `userid` *[integer]*: user who submitted the answers
- `genre.a_cappella`...`genre.worship` *[integer]*: 1:liked, 0:otherwise

## moodactivity.csv

Each row represents one task where users were given a mood term and a list of activities. The following question was presented: "Check all activities that in your opinion fit music expressing the mood {`mood`}" (18559 rows, 11 columns)
- `userid` *[integer]*: user
- `mood` *[string]*: mood name
- `activity.daily_routines`...`activity.social` *[integer]*: value for each activity (1:checked, 0:not checked, *missing*:mood was skipped (unfamiliar mood))

## searches.csv

Each row represents one search task. First, a user was given a list of moods and were presented a question: "Select a mood term that you can associate with a music example". Then a track was searched and submitted ("Search and submit a music example that expresses the mood {selected mood}"). Finally, activities were associated for the track ("Check all activities that fit the selected track expressing the mood {selected mood}").  (8681 rows, 99 columns)
- `userid` *[integer]*: user
- `trackid` *[integer]*: track
- `mood.adorable`...`mood.uplifting` *[integer]*: value for each mood (1: mood was selected, 0: mood was not selected, *missing*: mood wasn't included in the list)
- `activity.daily_routines`...`activity.social` *[integer]*: value for each activity (1:checked, 0:not checked)

## tags.csv

Each row represents one tagging task. First, a user was asked to listen a given music example and was presented a list of moods. The user was then asked to tag the exmple with moods ("Check zero or more moods that the music example expresses"). Finally, activities were associated for the track ("Check all activities that in your opinion fit the music clip") (28550 rows, 99 columns)
- `userid` *[integer]*: user
- `trackid` *[integer]*: track
- `mood.adorable`...`mood.uplifting` *[integer]*: value for each mood (1: mood was applied as a tag, 0: mood was not applied, *missing*: mood wasn't included in the list)
- `activity.daily_routines`...`activity.social` *[integer]*: value for each activity (1:checked, 0:not checked)

## test_tags.csv

Each row represents one consistency check (user had been given this music example before). Structure similar to tags.csv, but includes only moods. (6777 rows, 90 columns)
- `userid` *[integer]*: user
- `trackid` *[integer]*: track
- `mood.adorable`...`mood.uplifting` *[integer]*: (1: mood was applied as a tag, 0: mood was not applied, *missing*: mood wasn't included in the list)