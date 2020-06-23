# SURGE
The overall goal of this for this project is to help predict social unrest. With worldwide instability and unrest, the Social Unrest Reconnaissance GazEtteer (SURGE) project was created to predict this underlying problem. It emphasizes making long-term predictions using dynamic social media data and multiagent simulations. This project’s overall goal is to devise a system--integrating data, creating novel algorithms, and conducting multi agent simulations--that automatically and accurately anticipate social unrest events. With this project, the purpose is to improve on the current distance function used to identify a conceptual neighborhood of a social unrest event, to more effectively group similar unrest events. This, in turn, enables the system to more accurately predict social unrest by including influences or impacts from neighboring events. A conceptual neighborhood is beyond just spatial distances, as the distance function also involves temporal, social-economic, and infrastructural gaps. Specifically, in this project, we will observe how additional factors, mainly provided by the Global Database of Events, Language, and Tone (GDELT) database, can contribute to this distance function through the implementation of more positively influenced factors. With different variables, SPI is potentially one of many influencers of social unrest. We will be focusing specifically on SPI here. This project is funded by the NGA and lead by Dr. Soh at the University of Nebraska-Lincoln.

# What is SPI?
The Standardized Precipitation Index (SPI) was developed by McKee et al. (1993, 1995) as a widely used indicator to characterize meteorological drought, which standardizes the rainfall deficits/excess on a temporal and regional basis. SPI expresses the actual rainfall as a standardized departure with respect to rainfall probability distribution function permitting comparisons across space and time. Computation of SPI requires long term, typically 30-50 years of data on precipitation to determine the probability distribution function, which is then transformed to a normal distribution with a mean of zero and standard deviation of one.

The SPI was designed to quantify the precipitation deficit for multiple timescales. The timescales can be of any length, but McKee and others (1993) initially calculated the SPI for 3-, 6-,12-, 24- and 48-month timescales. Statistically, 1–24 months is the best practical range of application (Guttman, 1994, 1999).

The positive (negative) SPI values are greater (less) than the median precipitation that is zero because of the standardization. The magnitude of the departure from zero is a probabilistic measure of the severity of a wet (+) or dry (-) condition (WMO, 2012; Guttman, 1999). 
  
SPI Value | Condictions
------------ | -------------
2.0+ | Extremely Wet
1.5 to 1.99 | Very Wet
1.0 to 1.49 | Moderately Wet
-0.99 to 0.99 | Near Normal
-1.0 to -1.49 | Moderately Dry
-1.5 to -1.99 | Very Dry
-2.0 and less | Extremely Dry
