SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";

START TRANSACTION;

SET time_zone = "+00:00";

-- #region - Country (county)
CREATE TABLE IF NOT EXISTS `country` (
    `id` int(10) NOT NULL,
    `country` varchar(100) NOT NULL,
    `description` mediumtext DEFAULT NULL,
    `shelterId` smallint(6) NOT NULL,
    `default` enum('0', '1') NOT NULL,
    `createdById` int(10) DEFAULT NULL,
    `timeCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE = MyISAM DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_general_ci;

-- Indexes for table `country`
ALTER TABLE `country`
ADD PRIMARY KEY (`id`),
ADD UNIQUE KEY `country` (`shelterId`, `country`);

-- AUTO_INCREMENT for table `country`
ALTER TABLE `country`
MODIFY `id` int(10) NOT NULL AUTO_INCREMENT,
AUTO_INCREMENT = 1;

-- #endregion

-- #region Job Title
CREATE TABLE IF NOT EXISTS `jobTitle` (
    `id` int(10) NOT NULL,
    `title` varchar(50) NOT NULL,
    `description` text DEFAULT NULL,
    `shelterId` smallint(6) UNSIGNED NOT NULL,
    `default` enum('0', '1') NOT NULL DEFAULT '0',
    `createdById` int(10) DEFAULT NULL,
    `timeCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE = MyISAM DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_general_ci;

ALTER TABLE `jobTitle`
ADD PRIMARY KEY (`id`),
ADD UNIQUE KEY `jobTitle` (`shelterId`, `title`);

-- AUTO_INCREMENT for table `jobTitle`

ALTER TABLE `jobTitle`
MODIFY `id` int(10) NOT NULL AUTO_INCREMENT,
AUTO_INCREMENT = 1723;
-- #endregion

-- #region Person
CREATE TABLE IF NOT EXISTS `person` (
    `id` int(10) NOT NULL,
    `firstName` varchar(50) DEFAULT NULL,
    `middleName` varchar(50) DEFAULT NULL,
    `lastName` varchar(50) DEFAULT NULL,
    `nickName` varchar(50) DEFAULT NULL,
    `additionalNames` varchar(100) DEFAULT NULL,
    `businessName` varchar(100) DEFAULT NULL,
    `birthDate` datetime DEFAULT NULL,
    `anniversaryDate` datetime DEFAULT NULL,
    `sexId` int(10) DEFAULT NULL,
    `personHousingStatusId` int(10) DEFAULT NULL,
    `personHouseInspectionStatusId` int(10) DEFAULT NULL,
    `inspectionDate` datetime DEFAULT NULL,
    `IDTypeId` int(10) DEFAULT NULL,
    `IDNumber` varchar(50) DEFAULT NULL,
    `heardId` int(10) DEFAULT NULL,
    `homePhone` varchar(25) DEFAULT NULL,
    `workPhone` varchar(25) DEFAULT NULL,
    `cellPhone` varchar(25) DEFAULT NULL,
    `email` varchar(255) DEFAULT NULL,
    `email2` varchar(255) DEFAULT NULL,
    `address` varchar(100) DEFAULT NULL,
    `address2` varchar(100) DEFAULT NULL,
    `city` varchar(100) DEFAULT NULL,
    `region` varchar(50) DEFAULT NULL,
    `postalCode` varchar(10) DEFAULT NULL,
    `countryId` int(10) DEFAULT NULL,
    `commentsGeneral` mediumtext DEFAULT NULL,
    `commentsHidden` mediumtext DEFAULT NULL,
    `commentsHousing` mediumtext DEFAULT NULL,
    `commentsBanned` mediumtext DEFAULT NULL,
    `readyToDelete` enum('0', '1') NOT NULL DEFAULT '0',
    `banned` datetime DEFAULT NULL,
    `timeEntered` datetime NOT NULL,
    `shelterId` smallint(6) NOT NULL,
    `createdById` int(10) DEFAULT NULL,
    `timeCreated` timestamp NOT NULL DEFAULT current_timestamp(),
    `alert` text DEFAULT NULL,
    `county` varchar(45) DEFAULT NULL
) ENGINE = MyISAM DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_general_ci;

ALTER TABLE `person`
ADD PRIMARY KEY (`id`),
ADD KEY `shelterId` (`shelterId`),
ADD KEY `banned` (`shelterId`, `banned`),
ADD KEY `timeEntered` (`shelterId`, `timeEntered`),
ADD KEY `birthDate` (`shelterId`, `birthDate`),
ADD KEY `heardId` (`shelterId`, `heardId`),
ADD KEY `anniversaryDate` (
    `shelterId`,
    `anniversaryDate`
);

ALTER TABLE `person`
ADD FULLTEXT KEY `person` (
    `firstName`,
    `middleName`,
    `lastName`,
    `nickName`,
    `businessName`,
    `additionalNames`
);

ALTER TABLE `person`
MODIFY `id` int(10) NOT NULL AUTO_INCREMENT,
AUTO_INCREMENT = 409231;

-- #endregion

-- #region Staff
CREATE TABLE IF NOT EXISTS `staff` (
    `personId` int(10) NOT NULL,
    `current` enum('0', '1') NOT NULL DEFAULT '0',
    `volunteer` enum('0', '1') NOT NULL DEFAULT '0',
    `web` enum('0', '1') NOT NULL DEFAULT '0',
    `dateJoined` datetime DEFAULT NULL,
    `shortBio` varchar(255) DEFAULT NULL,
    `longBio` text DEFAULT NULL,
    `comments` text DEFAULT NULL,
    `commentsHidden` text DEFAULT NULL,
    `createdById` int(10) NOT NULL,
    `timeCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE = MyISAM DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_general_ci;

ALTER TABLE `staff`
ADD PRIMARY KEY (`personId`),
ADD KEY `current` (`current`),
ADD KEY `volunteer` (`volunteer`);

-- #endregion

-- #region Staff Job Title
CREATE TABLE IF NOT EXISTS `staffJobTitle` (
    `id` int(10) NOT NULL,
    `staffId` int(10) NOT NULL,
    `titleId` int(10) NOT NULL,
    `primary` enum('0', '1') NOT NULL DEFAULT '0',
    `createdById` int(10) NOT NULL,
    `timeCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE = MyISAM DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_general_ci;

ALTER TABLE `staffJobTitle`
ADD PRIMARY KEY (`id`),
ADD UNIQUE KEY `staffJobTitle` (`staffId`, `titleId`);

ALTER TABLE `staffJobTitle`
MODIFY `id` int(10) NOT NULL AUTO_INCREMENT,
AUTO_INCREMENT = 5485;
-- #endregion

-- #region signInType (teams)
CREATE TABLE IF NOT EXISTS `signInType` (
    `id` int(10) NOT NULL,
    `type` varchar(100) NOT NULL,
    `description` text DEFAULT NULL,
    `shelterId` smallint(6) NOT NULL,
    `default` enum('0', '1') NOT NULL,
    `createdById` int(10) DEFAULT NULL,
    `timeCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE = MyISAM DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_general_ci;

ALTER TABLE `signInType`
ADD PRIMARY KEY (`id`),
ADD KEY `signInType` (`shelterId`, `type`);

ALTER TABLE `signInType`
MODIFY `id` int(10) NOT NULL AUTO_INCREMENT,
AUTO_INCREMENT = 4815;

-- #endregion

-- #region desiredJobs (team assignments)
CREATE TABLE `desiredJob` (
    `id` int(10) NOT NULL,
    `staffId` int(10) NOT NULL,
    `jobId` int(10) NOT NULL,
    `createdById` int(10) NOT NULL,
    `timeCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE = MyISAM DEFAULT CHARSET = utf8mb3 COLLATE = utf8mb3_general_ci;

ALTER TABLE `desiredJob`
ADD PRIMARY KEY (`id`),
ADD UNIQUE KEY `desiredJob` (`staffId`, `jobId`);

ALTER TABLE `desiredJob`
MODIFY `id` int(10) NOT NULL AUTO_INCREMENT,
AUTO_INCREMENT = 71906;

# endregion
-- commit everything
COMMIT;