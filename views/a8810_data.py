from datetime import datetime, timedelta

utc_timestamps =[datetime.utcnow() + timedelta(minutes=-1), ]
for i in range(1, 59):
    t = utc_timestamps[-1]
    utc_timestamps.append(t + timedelta(seconds=1))

timestamps = [ts.strftime('%Y-%m-%d %H:%M:%S') for ts in utc_timestamps]

xmldata = """<?xml version="1.0" encoding="UTF-8" ?>
<DAS>
<mode>LOGFILEUPLOAD</mode>
<name>AMP-SHARK</name>
<serial>001EC605215F</serial>
<devices>
<device>
<name>SHARK - INVERTER</name>
<address>11</address>
<type>Shark 100</type>
<class>35</class>
<numpoints>116</numpoints>
<records>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.89" />
<point number="1" name="Volts B-N" units="Volts" value="120.11" />
<point number="2" name="Volts C-N" units="Volts" value="122.41" />
<point number="3" name="Volts A-B" units="Volts" value="207.79" />
<point number="4" name="Volts B-C" units="Volts" value="209.98" />
<point number="5" name="Volts C-A" units="Volts" value="209.79" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18703" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-67.6" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.72" />
<point number="1" name="Volts B-N" units="Volts" value="119.89" />
<point number="2" name="Volts C-N" units="Volts" value="122.27" />
<point number="3" name="Volts A-B" units="Volts" value="207.48" />
<point number="4" name="Volts B-C" units="Volts" value="209.67" />
<point number="5" name="Volts C-A" units="Volts" value="209.53" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18721" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18656" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18953" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-70.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.74" />
<point number="1" name="Volts B-N" units="Volts" value="119.93" />
<point number="2" name="Volts C-N" units="Volts" value="122.30" />
<point number="3" name="Volts A-B" units="Volts" value="207.49" />
<point number="4" name="Volts B-C" units="Volts" value="209.68" />
<point number="5" name="Volts C-A" units="Volts" value="209.54" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18721" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18656" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.76" />
<point number="1" name="Volts B-N" units="Volts" value="119.95" />
<point number="2" name="Volts C-N" units="Volts" value="122.31" />
<point number="3" name="Volts A-B" units="Volts" value="207.50" />
<point number="4" name="Volts B-C" units="Volts" value="209.70" />
<point number="5" name="Volts C-A" units="Volts" value="209.55" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18721" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18656" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.77" />
<point number="1" name="Volts B-N" units="Volts" value="119.97" />
<point number="2" name="Volts C-N" units="Volts" value="122.33" />
<point number="3" name="Volts A-B" units="Volts" value="207.51" />
<point number="4" name="Volts B-C" units="Volts" value="209.71" />
<point number="5" name="Volts C-A" units="Volts" value="209.57" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18656" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.78" />
<point number="1" name="Volts B-N" units="Volts" value="119.98" />
<point number="2" name="Volts C-N" units="Volts" value="122.33" />
<point number="3" name="Volts A-B" units="Volts" value="207.53" />
<point number="4" name="Volts B-C" units="Volts" value="209.73" />
<point number="5" name="Volts C-A" units="Volts" value="209.58" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18656" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.79" />
<point number="1" name="Volts B-N" units="Volts" value="119.99" />
<point number="2" name="Volts C-N" units="Volts" value="122.34" />
<point number="3" name="Volts A-B" units="Volts" value="207.54" />
<point number="4" name="Volts B-C" units="Volts" value="209.75" />
<point number="5" name="Volts C-A" units="Volts" value="209.59" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.56" />
<point number="4" name="Volts B-C" units="Volts" value="209.76" />
<point number="5" name="Volts C-A" units="Volts" value="209.61" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.57" />
<point number="4" name="Volts B-C" units="Volts" value="209.78" />
<point number="5" name="Volts C-A" units="Volts" value="209.62" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.97" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.58" />
<point number="4" name="Volts B-C" units="Volts" value="209.79" />
<point number="5" name="Volts C-A" units="Volts" value="209.63" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.59" />
<point number="4" name="Volts B-C" units="Volts" value="209.80" />
<point number="5" name="Volts C-A" units="Volts" value="209.64" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18740" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.01" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.60" />
<point number="4" name="Volts B-C" units="Volts" value="209.81" />
<point number="5" name="Volts C-A" units="Volts" value="209.65" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18740" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.01" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.61" />
<point number="4" name="Volts B-C" units="Volts" value="209.82" />
<point number="5" name="Volts C-A" units="Volts" value="209.66" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18740" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18674" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.01" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.62" />
<point number="4" name="Volts B-C" units="Volts" value="209.83" />
<point number="5" name="Volts C-A" units="Volts" value="209.66" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18740" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18674" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.02" />
<point number="2" name="Volts C-N" units="Volts" value="122.37" />
<point number="3" name="Volts A-B" units="Volts" value="207.63" />
<point number="4" name="Volts B-C" units="Volts" value="209.84" />
<point number="5" name="Volts C-A" units="Volts" value="209.67" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18740" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18674" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18974" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.02" />
<point number="2" name="Volts C-N" units="Volts" value="122.37" />
<point number="3" name="Volts A-B" units="Volts" value="207.64" />
<point number="4" name="Volts B-C" units="Volts" value="209.85" />
<point number="5" name="Volts C-A" units="Volts" value="209.68" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18740" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18674" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18974" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.37" />
<point number="3" name="Volts A-B" units="Volts" value="207.64" />
<point number="4" name="Volts B-C" units="Volts" value="209.85" />
<point number="5" name="Volts C-A" units="Volts" value="209.69" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18674" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18974" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="119.99" />
<point number="2" name="Volts C-N" units="Volts" value="122.37" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.86" />
<point number="5" name="Volts C-A" units="Volts" value="209.69" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18674" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18974" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="119.98" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.86" />
<point number="5" name="Volts C-A" units="Volts" value="209.70" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18664" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18974" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="119.97" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.86" />
<point number="5" name="Volts C-A" units="Volts" value="209.70" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18664" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18974" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="119.96" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.86" />
<point number="5" name="Volts C-A" units="Volts" value="209.70" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.032" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18664" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="119.97" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.86" />
<point number="5" name="Volts C-A" units="Volts" value="209.70" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18664" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="119.98" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.86" />
<point number="5" name="Volts C-A" units="Volts" value="209.70" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18664" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="119.98" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.86" />
<point number="5" name="Volts C-A" units="Volts" value="209.70" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18664" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-70.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.65" />
<point number="4" name="Volts B-C" units="Volts" value="209.87" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-70.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.66" />
<point number="4" name="Volts B-C" units="Volts" value="209.87" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-70.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-77.1" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.34" />
<point number="3" name="Volts A-B" units="Volts" value="207.66" />
<point number="4" name="Volts B-C" units="Volts" value="209.87" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-70.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-77.1" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.01" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.66" />
<point number="4" name="Volts B-C" units="Volts" value="209.87" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18744" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-77.1" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.01" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.67" />
<point number="4" name="Volts B-C" units="Volts" value="209.87" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-77.1" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-77.1" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.00" />
<point number="2" name="Volts C-N" units="Volts" value="122.34" />
<point number="3" name="Volts A-B" units="Volts" value="207.67" />
<point number="4" name="Volts B-C" units="Volts" value="209.87" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-77.1" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-75.5" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.01" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.67" />
<point number="4" name="Volts B-C" units="Volts" value="209.88" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-77.1" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-75.5" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.02" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.67" />
<point number="4" name="Volts B-C" units="Volts" value="209.88" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-77.1" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-75.5" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.02" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.68" />
<point number="4" name="Volts B-C" units="Volts" value="209.88" />
<point number="5" name="Volts C-A" units="Volts" value="209.71" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-77.1" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.02" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.68" />
<point number="4" name="Volts B-C" units="Volts" value="209.88" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-77.1" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.02" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.68" />
<point number="4" name="Volts B-C" units="Volts" value="209.89" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18738" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-77.1" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.03" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.69" />
<point number="4" name="Volts B-C" units="Volts" value="209.89" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18738" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18686" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.80" />
<point number="1" name="Volts B-N" units="Volts" value="120.03" />
<point number="2" name="Volts C-N" units="Volts" value="122.34" />
<point number="3" name="Volts A-B" units="Volts" value="207.69" />
<point number="4" name="Volts B-C" units="Volts" value="209.89" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.042" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18738" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.04" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.69" />
<point number="4" name="Volts B-C" units="Volts" value="209.89" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18738" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18964" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.81" />
<point number="1" name="Volts B-N" units="Volts" value="120.05" />
<point number="2" name="Volts C-N" units="Volts" value="122.35" />
<point number="3" name="Volts A-B" units="Volts" value="207.70" />
<point number="4" name="Volts B-C" units="Volts" value="209.90" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18738" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.05" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.70" />
<point number="4" name="Volts B-C" units="Volts" value="209.90" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18738" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.82" />
<point number="1" name="Volts B-N" units="Volts" value="120.05" />
<point number="2" name="Volts C-N" units="Volts" value="122.37" />
<point number="3" name="Volts A-B" units="Volts" value="207.70" />
<point number="4" name="Volts B-C" units="Volts" value="209.91" />
<point number="5" name="Volts C-A" units="Volts" value="209.72" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.0" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.83" />
<point number="1" name="Volts B-N" units="Volts" value="120.06" />
<point number="2" name="Volts C-N" units="Volts" value="122.38" />
<point number="3" name="Volts A-B" units="Volts" value="207.71" />
<point number="4" name="Volts B-C" units="Volts" value="209.91" />
<point number="5" name="Volts C-A" units="Volts" value="209.73" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.032" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18682" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-67.6" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.84" />
<point number="1" name="Volts B-N" units="Volts" value="120.07" />
<point number="2" name="Volts C-N" units="Volts" value="122.38" />
<point number="3" name="Volts A-B" units="Volts" value="207.71" />
<point number="4" name="Volts B-C" units="Volts" value="209.92" />
<point number="5" name="Volts C-A" units="Volts" value="209.73" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18697" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-67.6" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.84" />
<point number="1" name="Volts B-N" units="Volts" value="120.07" />
<point number="2" name="Volts C-N" units="Volts" value="122.38" />
<point number="3" name="Volts A-B" units="Volts" value="207.72" />
<point number="4" name="Volts B-C" units="Volts" value="209.92" />
<point number="5" name="Volts C-A" units="Volts" value="209.74" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.042" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18697" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-67.6" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.84" />
<point number="1" name="Volts B-N" units="Volts" value="120.08" />
<point number="2" name="Volts C-N" units="Volts" value="122.38" />
<point number="3" name="Volts A-B" units="Volts" value="207.73" />
<point number="4" name="Volts B-C" units="Volts" value="209.93" />
<point number="5" name="Volts C-A" units="Volts" value="209.74" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.042" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18697" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18982" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.85" />
<point number="1" name="Volts B-N" units="Volts" value="120.08" />
<point number="2" name="Volts C-N" units="Volts" value="122.39" />
<point number="3" name="Volts A-B" units="Volts" value="207.73" />
<point number="4" name="Volts B-C" units="Volts" value="209.94" />
<point number="5" name="Volts C-A" units="Volts" value="209.75" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.042" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18697" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18982" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-75.5" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.85" />
<point number="1" name="Volts B-N" units="Volts" value="120.09" />
<point number="2" name="Volts C-N" units="Volts" value="122.39" />
<point number="3" name="Volts A-B" units="Volts" value="207.74" />
<point number="4" name="Volts B-C" units="Volts" value="209.94" />
<point number="5" name="Volts C-A" units="Volts" value="209.75" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18697" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18982" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-75.5" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.85" />
<point number="1" name="Volts B-N" units="Volts" value="120.08" />
<point number="2" name="Volts C-N" units="Volts" value="122.37" />
<point number="3" name="Volts A-B" units="Volts" value="207.74" />
<point number="4" name="Volts B-C" units="Volts" value="209.95" />
<point number="5" name="Volts C-A" units="Volts" value="209.75" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.042" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18697" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18982" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-75.5" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.84" />
<point number="1" name="Volts B-N" units="Volts" value="120.07" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.75" />
<point number="4" name="Volts B-C" units="Volts" value="209.95" />
<point number="5" name="Volts C-A" units="Volts" value="209.75" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18688" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18982" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-75.5" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.85" />
<point number="1" name="Volts B-N" units="Volts" value="120.07" />
<point number="2" name="Volts C-N" units="Volts" value="122.36" />
<point number="3" name="Volts A-B" units="Volts" value="207.75" />
<point number="4" name="Volts B-C" units="Volts" value="209.95" />
<point number="5" name="Volts C-A" units="Volts" value="209.76" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18688" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18982" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.86" />
<point number="1" name="Volts B-N" units="Volts" value="120.08" />
<point number="2" name="Volts C-N" units="Volts" value="122.37" />
<point number="3" name="Volts A-B" units="Volts" value="207.76" />
<point number="4" name="Volts B-C" units="Volts" value="209.95" />
<point number="5" name="Volts C-A" units="Volts" value="209.76" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18688" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-77.1" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.87" />
<point number="1" name="Volts B-N" units="Volts" value="120.09" />
<point number="2" name="Volts C-N" units="Volts" value="122.38" />
<point number="3" name="Volts A-B" units="Volts" value="207.76" />
<point number="4" name="Volts B-C" units="Volts" value="209.96" />
<point number="5" name="Volts C-A" units="Volts" value="209.76" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18688" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-77.1" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.88" />
<point number="1" name="Volts B-N" units="Volts" value="120.10" />
<point number="2" name="Volts C-N" units="Volts" value="122.40" />
<point number="3" name="Volts A-B" units="Volts" value="207.77" />
<point number="4" name="Volts B-C" units="Volts" value="209.96" />
<point number="5" name="Volts C-A" units="Volts" value="209.77" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.042" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.99" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18688" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-77.1" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.88" />
<point number="1" name="Volts B-N" units="Volts" value="120.10" />
<point number="2" name="Volts C-N" units="Volts" value="122.39" />
<point number="3" name="Volts A-B" units="Volts" value="207.78" />
<point number="4" name="Volts B-C" units="Volts" value="209.97" />
<point number="5" name="Volts C-A" units="Volts" value="209.78" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18688" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.88" />
<point number="1" name="Volts B-N" units="Volts" value="120.10" />
<point number="2" name="Volts C-N" units="Volts" value="122.40" />
<point number="3" name="Volts A-B" units="Volts" value="207.78" />
<point number="4" name="Volts B-C" units="Volts" value="209.97" />
<point number="5" name="Volts C-A" units="Volts" value="209.78" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18703" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18972" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-75.5" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.89" />
<point number="1" name="Volts B-N" units="Volts" value="120.11" />
<point number="2" name="Volts C-N" units="Volts" value="122.41" />
<point number="3" name="Volts A-B" units="Volts" value="207.80" />
<point number="4" name="Volts B-C" units="Volts" value="209.99" />
<point number="5" name="Volts C-A" units="Volts" value="209.80" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18703" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18986" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-67.6" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-74.9" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.90" />
<point number="1" name="Volts B-N" units="Volts" value="120.11" />
<point number="2" name="Volts C-N" units="Volts" value="122.41" />
<point number="3" name="Volts A-B" units="Volts" value="207.80" />
<point number="4" name="Volts B-C" units="Volts" value="209.99" />
<point number="5" name="Volts C-A" units="Volts" value="209.80" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18752" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18703" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18986" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-67.6" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.89" />
<point number="1" name="Volts B-N" units="Volts" value="120.11" />
<point number="2" name="Volts C-N" units="Volts" value="122.40" />
<point number="3" name="Volts A-B" units="Volts" value="207.81" />
<point number="4" name="Volts B-C" units="Volts" value="209.99" />
<point number="5" name="Volts C-A" units="Volts" value="209.80" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18703" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18986" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-74.9" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
<record>
<time zone="UTC">%s</time>
<error text="Ok">0</error>
<point number="0" name="Volts A-N" units="Volts" value="119.90" />
<point number="1" name="Volts B-N" units="Volts" value="120.12" />
<point number="2" name="Volts C-N" units="Volts" value="122.41" />
<point number="3" name="Volts A-B" units="Volts" value="207.81" />
<point number="4" name="Volts B-C" units="Volts" value="210.00" />
<point number="5" name="Volts C-A" units="Volts" value="209.81" />
<point number="6" name="Amps A" units="Amps" value="0.11" />
<point number="7" name="Amps B" units="Amps" value="0.12" />
<point number="8" name="Amps C" units="Amps" value="0.12" />
<point number="9" name="Watts, 3-Ph total" units="kW" value="0.011" />
<point number="10" name="VARs, 3-Ph total" units="kVAR" value="0.040" />
<point number="11" name="VAs, 3-Ph total" units="kVA" value="0.041" />
<point number="12" name="Power Factor, 3-Ph total" units="" value="0.27" />
<point number="13" name="Frequency" units="Hz" value="59.98" />
<point number="14" name="Neutral Current" units="Amps" value="0" />
<point number="15" name="W-hours, Received" units="kWh" value="32" />
<point number="16" name="W-hours, Delivered" units="kWh" value="-3" />
<point number="17" name="W-hours, Net" units="kWh" value="28" />
<point number="18" name="W-hours, Total" units="kWh" value="35" />
<point number="19" name="VAR-hours, Positive" units="kVARh" value="117" />
<point number="20" name="VAR-hours, Negative" units="kVARh" value="-1" />
<point number="21" name="VAR-hours, Net" units="kVARh" value="116" />
<point number="22" name="VAR-hours, Total" units="kVARh" value="119" />
<point number="23" name="VA-hours, Total" units="kVAh" value="126" />
<point number="24" name="Amps A, Average" units="Amps" value="0.10" />
<point number="25" name="Amps B, Average" units="Amps" value="0.12" />
<point number="26" name="Amps C, Average" units="Amps" value="0.12" />
<point number="27" name="Positive Watts, 3-Ph, Average" units="kW" value="0.011" />
<point number="28" name="Positive VARs, 3-Ph, Average" units="kVAR" value="0.039" />
<point number="29" name="Negative Watts, 3-Ph, Average" units="kW" value="0" />
<point number="30" name="Negative VARs, 3-Ph, Average" units="kVAR" value="0" />
<point number="31" name="VAs, 3-Ph, Average" units="kVA" value="0.041" />
<point number="32" name="Positive PF, 3-Ph, Average" units="" value="0.27" />
<point number="33" name="Negative PF, 3-Ph, Average" units="" value="0" />
<point number="34" name="Volts A-N, Min" units="Volts" value="0" />
<point number="35" name="Volts B-N, Min" units="Volts" value="0" />
<point number="36" name="Volts C-N, Min" units="Volts" value="0" />
<point number="37" name="Volts A-B, Min" units="Volts" value="0" />
<point number="38" name="Volts B-C, Min" units="Volts" value="0" />
<point number="39" name="Volts C-A, Min" units="Volts" value="0" />
<point number="40" name="Amps A, Min Avg Demand" units="Amps" value="0" />
<point number="41" name="Amps B, Min Avg Demand" units="Amps" value="0" />
<point number="42" name="Amps C, Min Avg Demand" units="Amps" value="0" />
<point number="43" name="Positive Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="44" name="Positive VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="45" name="Negative Watts, 3-Ph, Min Avg Demand" units="kW" value="0" />
<point number="46" name="Negative VARs, 3-Ph Min Avg Demand" units="kVAR" value="0" />
<point number="47" name="VAs, 3-Ph, Min Avg Demand" units="kVA" value="0" />
<point number="48" name="Positive PF, 3-Ph, Min Avg Demand" units="" value="1.00" />
<point number="49" name="Negative PF, 3-Ph, Min Avg Demand" units="" value="-0.97" />
<point number="50" name="Frequency, Min" units="Hz" value="0" />
<point number="51" name="Volts A-N, Max" units="Volts" value="124.71" />
<point number="52" name="Volts B-N, Max" units="Volts" value="125.01" />
<point number="53" name="Volts C-N, Max" units="Volts" value="127.15" />
<point number="54" name="Volts A-B, Max" units="Volts" value="216.25" />
<point number="55" name="Volts B-C, Max" units="Volts" value="218.38" />
<point number="56" name="Volts C-A, Max" units="Volts" value="218.12" />
<point number="57" name="Amps A, Max Avg Demand" units="Amps" value="6.91" />
<point number="58" name="Amps B, Max Avg Demand" units="Amps" value="7.09" />
<point number="59" name="Amps C, Max Avg Demand" units="Amps" value="6.96" />
<point number="60" name="Positive Watts, 3-Ph, Max Avg Demand" units="kW" value="1.247" />
<point number="61" name="Positive VARs, 3-Ph Max Avg Demand" units="kVAR" value="1.420" />
<point number="62" name="Negative Watts, 3-Ph, Max Avg Demand" units="kW" value="-2.437" />
<point number="63" name="Negative VARs, 3-Ph Max Avg Demand" units="kVAR" value="-1.769" />
<point number="64" name="VAs, 3-Ph, Max Avg Demand" units="kVA" value="2.519" />
<point number="65" name="Positive PF, 3-Ph, Max Avg Demand" units="" value="0" />
<point number="66" name="Negative PF, 3-Ph, Max Avg Demand" units="" value="1.00" />
<point number="67" name="Frequency, Max" units="Hz" value="60.47" />
<point number="68" name="Volts A-N, %%THD" units="%%" value="0" />
<point number="69" name="Volts B-N, %%THD" units="%%" value="0" />
<point number="70" name="Volts C-N, %%THD" units="%%" value="0" />
<point number="71" name="Amps A, %%THD" units="%%" value="NULL" />
<point number="72" name="Amps B, %%THD" units="%%" value="NULL" />
<point number="73" name="Amps C, %%THD" units="%%" value="NULL" />
<point number="74" name="Phase A Current 0th harmonic magnitude" units="" value="65535" />
<point number="75" name="Phase A Current 1st harmonic magnitude" units="" value="65535" />
<point number="76" name="Phase A Current 2nd harmonic magnitude" units="" value="65535" />
<point number="77" name="Phase A Current 3rd harmonic magnitude" units="" value="65535" />
<point number="78" name="Phase A Current 4th harmonic magnitude" units="" value="65535" />
<point number="79" name="Phase A Current 5th harmonic magnitude" units="" value="65535" />
<point number="80" name="Phase A Current 6th harmonic magnitude" units="" value="65535" />
<point number="81" name="Phase A Current 7th harmonic magnitude" units="" value="65535" />
<point number="82" name="Phase A Voltage 0th harmonic magnitude" units="" value="18754" />
<point number="83" name="Phase A Voltage 1st harmonic magnitude" units="" value="0" />
<point number="84" name="Phase A Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="85" name="Phase A Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="86" name="Phase B Current 0th harmonic magnitude" units="" value="65535" />
<point number="87" name="Phase B Current 1st harmonic magnitude" units="" value="65535" />
<point number="88" name="Phase B Current 2nd harmonic magnitude" units="" value="65535" />
<point number="89" name="Phase B Current 3rd harmonic magnitude" units="" value="65535" />
<point number="90" name="Phase B Current 4th harmonic magnitude" units="" value="65535" />
<point number="91" name="Phase B Current 5th harmonic magnitude" units="" value="65535" />
<point number="92" name="Phase B Current 6th harmonic magnitude" units="" value="65535" />
<point number="93" name="Phase B Current 7th harmonic magnitude" units="" value="65535" />
<point number="94" name="Phase B Voltage 0th harmonic magnitude" units="" value="18703" />
<point number="95" name="Phase B Voltage 1st harmonic magnitude" units="" value="0" />
<point number="96" name="Phase B Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="97" name="Phase B Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="98" name="Phase C Current 0th harmonic magnitude" units="" value="65535" />
<point number="99" name="Phase C Current 1st harmonic magnitude" units="" value="65535" />
<point number="100" name="Phase C Current 2nd harmonic magnitude" units="" value="65535" />
<point number="101" name="Phase C Current 3rd harmonic magnitude" units="" value="65535" />
<point number="102" name="Phase C Current 4th harmonic magnitude" units="" value="65535" />
<point number="103" name="Phase C Current 5th harmonic magnitude" units="" value="65535" />
<point number="104" name="Phase C Current 6th harmonic magnitude" units="" value="65535" />
<point number="105" name="Phase C Current 7th harmonic magnitude" units="" value="65535" />
<point number="106" name="Phase C Voltage 0th harmonic magnitude" units="" value="18986" />
<point number="107" name="Phase C Voltage 1st harmonic magnitude" units="" value="0" />
<point number="108" name="Phase C Voltage 2nd harmonic magnitude" units="" value="0" />
<point number="109" name="Phase C Voltage 3rd harmonic magnitude" units="" value="0" />
<point number="110" name="Angle, Phase A Current" units="Degrees" value="-73.3" />
<point number="111" name="Angle, Phase B Current" units="Degrees" value="-73.0" />
<point number="112" name="Angle, Phase C Current" units="Degrees" value="-73.0" />
<point number="113" name="Angle, Volts A-B" units="Degrees" value="120.0" />
<point number="114" name="Angle, Volts B-C" units="Degrees" value="120.0" />
<point number="115" name="Angle, Volts C-A" units="Degrees" value="120.0" />
</record>
</records>
</device>
</devices>
</DAS>""" % tuple(timestamps)

def get_data():
    return xmldata

if __name__ == '__main__':
 print get_data()
