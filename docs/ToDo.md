# ToDo

## Phase 1 
The goal of this phase is to have a proof of concert that can used for testing. It should not be a standalone application, however it should have a user friendly UI for people without programming knowledge. 

The application developed in this phase will be created in Python.

### Functionallity 
- [ ] Setup Github reposetory from a standard template
- [ ] Ability to apply filters to a still image
- [ ] Ability to apply filters to a video file
- [x] Ability to apply filters to live screen capture

### Filters
- [ ] Create a unsharp filter
- [ ] Create a Gausian filter
- [ ] Create option for running filter multiple times
- [ ] Create option for changing kernal size of the filter 
- [ ] Create option for changing each color channel intensity - warm/cold colors

### UI
- [ ] Create UI window that can be open/closed with all options
- [ ] Create toggle for filter on/off
- [ ] Create filter select menu
- [ ] Slider to change the kernal size of the filter
- [ ] Be able to select filter settings for all 3 color channels (filter type, amount of time the filter is applied, kernal size)
- [ ] 

### Documentation / Visual representation (Only for images)
- [ ] Show a color channel in the spectrial domain before and after a filter has been added. 


## Phase 2
The goal of this phase is create a standalone application, that an ordinary person can download, install and use. The application should atleast run on either a pc, laptop or portable device such as a phone. 

The application developed in this phase will most likely be created in c, c++ or c#.

### Functionallity 
- [ ] Ability to run filters as a background application on Windows or Linux
- [ ] Ability to run filters as a background application on Android or IOS


### Filters
- [ ] Create an option to ignore the filter in a certian area on the screen. This could e.g. be a circle area around the mouse position.
- [ ] If applicable, implement other filters.
