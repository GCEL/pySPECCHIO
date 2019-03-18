# -*- coding: utf-8 -*-

# Created on Wed Apr 18 17:08:38 2018

# @author: dvalters

# PICO SPECTRA METADATA
# ADD METADATA VALUES
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Dark', (select category_id from `specchio`.category where name ='General'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Dark');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Datetime', (select category_id from `specchio`.category where name ='General'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Datetime');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Direction', (select category_id from `specchio`.category where name ='General'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Direction');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Integration Time Units', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Integration Time Units');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Nonlinearity Correction Coefficients', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Nonlinearity Correction Coefficients');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Optical Pixel Range', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Optical Pixel Range');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Run', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Run');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Saturation Level', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'double_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Saturation Level');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Temperature Detector Actual', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'double_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Temperature Detector Actual');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Temperature Detector Set', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'double_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Temperature Detector Set');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Temperature Detector Heatsink', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'double_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Temperature Detector Heatsink');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Temperature Detector Microcontroller', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'double_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Temperature Detector Microcontroller');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Temperature Detector PCB', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'double_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Temperature Detector PCB');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Temperature Units', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Temperature Detector Units');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Type', (select category_id from `specchio`.category where name ='General'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Type');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('Wavelength Calibration Coefficients', (select category_id from `specchio`.category where name ='Instrument Settings'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'Wavelength Calibration Coefficients');
INSERT INTO `specchio`.`attribute`(`name`, `category_id`, `default_storage_field`, `default_unit_id`, `description`)
 VALUES ('name', (select category_id from `specchio`.category where name ='General'),
 'string_val', (select unit_id from `specchio`.unit where short_name = ''), 
 'name');


# Categories

INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('26', 'Fluorescence', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('27', 'GS', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('28', 'Harvest', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('29', 'CN', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('30', 'HI', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('31', 'Height', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('32', 'LAI', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('33', 'SPAD', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('34', 'ThetaProbe', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('35', 'NitrateAmmonia', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('36', 'ResinExtracts', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('37', 'Moisture', '');
INSERT INTO `specchio`.`category` (`category_id`, `name`, `string_val`) VALUES ('38', 'pH', '');

# Attributes METADATA FROM ANCIL DATA

INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('402', 'Fertiliser_level', 'Fertiliser Level (GS)', '27', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('403', 'GS', 'GS', '27', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('404', 'Fertiliser_level', 'Fertiliser Level (Harvest)', '28', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('405', 'Yield_TonnesPerHectare', 'Yield Tonnes per Hectare', '28', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('406', 'TGW', 'TGW', '28', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('407', 'FreshWeightKg', 'FreshWeightKg', '28', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('408', 'DryMatter%', 'Dry Matter Percentage', '28', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('409', 'no_in15g', 'no_in15g', '28', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('410', 'Fertiliser_level', 'Fertiliser Level (CN)', '29', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('411', 'N%', 'Nitrogen Percentage', '29', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('412', 'C%', 'Carbon Percentage', '29', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('413', 'Fertiliser_level', 'Fertiliser Level (HI)', '30', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('414', 'StrawFreshWeight', 'Straw Fresh Weight', '30', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('415', 'StrawDryWeight', 'Straw Dry Weight', '30', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('416', 'WholeEarWeight', 'Whole Ear Weight', '30', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('417', 'GrainWeight', 'Grain Weight', '30', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('418', 'ChaffWeight', 'Chaff Weight', '30', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('419', 'HI', 'HI', '30', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('420', 'Fertiliser_level', 'Fertiliser Level (Height)', '31', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('421', 'Height1', 'Height1', '31', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('422', 'Height2', 'Height2', '31', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('423', 'Height3', 'Height3', '31', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('424', 'Height4', 'Height4', '31', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('425', 'Height5', 'Height5', '31', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('426', 'Plot_height', 'Plot_height', '31', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`, `cardinality`) VALUES ('427', 'Fertiliser_level', 'Fertiliser Level (SPAD)', '33', 'double_val', '1');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('428', 'SPAD1', 'SPAD1', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('429', 'SPAD2', 'SPAD2', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('430', 'SPAD3', 'SPAD3', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('431', 'SPAD4', 'SPAD4', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('432', 'SPAD5', 'SPAD5', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('433', 'SPAD6', 'SPAD6', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('434', 'SPAD7', 'SPAD7', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('435', 'SPAD8', 'SPAD8', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('436', 'SPAD9', 'SPAD9', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('437', 'SPAD10', 'SPAD10', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('438', 'Plot_Average', 'Plot Average SPAD', '33', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('439', 'Fertiliser_level', 'Fertiliser Level (ThetaProbe)', '34', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('440', 'Moisture1', 'Moisture1', '34', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('441', 'Moisture2', 'Moisture2', '34', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('442', 'Moisture3', 'Moisture3', '34', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('443', 'Moisture4', 'Moisture4', '34', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('444', 'Moisture5', 'Moisture5', '34', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('445', 'Plot Moisture', 'Plot Moisture', '34', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('446', 'Fertiliser_level', 'Fertiliser Level (NitrateAmmonia)', '35', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('447', 'NO2NO3mgperlN', 'NO2NO3mgperlN', '35', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('448', 'AmmoniamgperlN', 'AmmoniamgperlN', '35', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('449', 'Fertiliser_level', 'Fertiliser Level (ResinExtracts)', '36', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('450', 'Ammonia_set1', 'Ammonia_set1', '36', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('451', 'Nitrate_set1', 'Nitrate_set1', '36', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('452', 'Fertiliser_level', 'Fertiliser Level (Moisture)', '37', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('453', 'Moisture%g/g', 'Moisture%g/g', '37', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('454', 'Fertiliser_level', 'Fertiliser Level (pH)', '38', 'double_val');
INSERT INTO `specchio`.`attribute` (`attribute_id`, `name`, `description`, `category_id`, `default_storage_field`) VALUES ('455', 'pH', 'pH', '38', 'double_val');

