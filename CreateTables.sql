CREATE TABLE Frames (
  FrameId INT PRIMARY KEY IDENTITY(1,1),
  Volume FLOAT,
	FrameTime DATETIME,
	StorageIdentifier INT
);

CREATE TABLE Points1(
  PointId INT PRIMARY KEY IDENTITY(1,1),
  FrameId INT FOREIGN KEY REFERENCES Frames(FrameId),
	X FLOAT,
	Y FLOAT,
	Z FLOAT,
	Distance FLOAT,
	Intensity FLOAt,
	Point_Id FLOAT,
	Return_Id FLOAT,
	Ambient FLOAT,
	Timestamp FLOAT
);
CREATE TABLE Points2(
  PointId INT PRIMARY KEY IDENTITY(1,1),
  FrameId INT FOREIGN KEY REFERENCES Frames(FrameId),
	X FLOAT,
	Y FLOAT,
	Z FLOAT,
	Distance FLOAT,
	Intensity FLOAt,
	Point_Id FLOAT,
	Return_Id FLOAT,
	Ambient FLOAT,
	Timestamp FLOAT
);
CREATE TABLE Points3(
  PointId INT PRIMARY KEY IDENTITY(1,1),
  FrameId INT FOREIGN KEY REFERENCES Frames(FrameId),
	X FLOAT,
	Y FLOAT,
	Z FLOAT,
	Distance FLOAT,
	Intensity FLOAt,
	Point_Id FLOAT,
	Return_Id FLOAT,
	Ambient FLOAT,
	Timestamp FLOAT
);
CREATE TABLE Points4(
  PointId INT PRIMARY KEY IDENTITY(1,1),
  FrameId INT FOREIGN KEY REFERENCES Frames(FrameId),
	X FLOAT,
	Y FLOAT,
	Z FLOAT,
	Distance FLOAT,
	Intensity FLOAt,
	Point_Id FLOAT,
	Return_Id FLOAT,
	Ambient FLOAT,
	Timestamp FLOAT
);