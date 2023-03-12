from midiutil.MidiFile import MIDIFile

class midinotes:
  def __init__(self, midi_file_format):
    self.debug = 0
    self.notes = []
    self.miditrackname = "Sample Track"
    self.tempo = 0
    self.track = 0
    print("initialize midifile...");
    self.mf = MIDIFile(1,file_format=int(midi_file_format))
    print("initialize midifile done.");

  def addNote(self,track, channel, note, start_time, duration, volume ):
    self.notes.append( {'track' : track, 'channel' : channel, 'note' : note, 'start_time' : start_time, 'duration' : duration, 'volume' : volume } )

  def sync_start_pos(self, time_delta = 0.25, abs_time_delta=False ):
    for i in range( len(self.notes) ):
      for j in range( i+1, len(self.notes) ):
        if abs_time_delta:
          if abs(self.notes[j]['start_time'] - self.notes[i]['start_time']) < time_delta:
            self.notes[j]['start_time'] = self.notes[i]['start_time']
        else:
          if self.notes[j]['start_time'] - self.notes[i]['start_time'] < time_delta:
            self.notes[j]['start_time'] = self.notes[i]['start_time']

  def setup_track(self, time, trackName, tempo ):
    self.miditrackname = trackName
    self.tempo = tempo
    self.mf.addTrackName(self.track, time, trackName)
    self.mf.addTempo(self.track, time, tempo )

  def addProgramChange(self, track, channel, program):
    self.mf.addProgramChange(track, channel, 0, program)

  def save_to_disk(self, filename):
    if len(self.notes) < 1:
      return 0, "No notes to save.."
    for i in self.notes:
      self.mf.addNote( i['track'], i['channel'], i['note'], i['start_time'], i['duration'], i['volume'] )
    try:
      with open(filename, 'wb') as outf:
        self.mf.writeFile(outf)
    except Exception as E:
      print("Error on save to disk:%s"% E)
      return -1, "Can't save to disk:%s" % filename
    return 1, "Saved to disk:%s" % filename
