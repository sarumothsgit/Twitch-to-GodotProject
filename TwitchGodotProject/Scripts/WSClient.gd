extends Node
var s_i: String = "WSC.gd:" #Websocket Client GDScript script

var ws_client = WebSocketPeer.new()
var url: String = "ws://localhost:1116"

var payload_flag: bool = false

func _ready():
	print(s_i + "_ready():")
	var error = ws_client.connect_to_url(url)
	if error != OK:
		set_process(false)

func _process(_delta):
	ws_client.poll()
	while ws_client.get_available_packet_count():
		print(s_i + "while ws_client.get_available_packet_count():")
		var packet = ws_client.get_packet().get_string_from_utf8()
		if packet:
			ws_packet_received(packet)

func ws_packet_received(packet):
	print(s_i + "ws_packet_received(packet):")
	payload_flag = true
	var payload = packet
	process_payload(payload)

func process_payload(payload):
	print(s_i + "process_payload(payload):")
	if payload != null:
		if payload_flag == true:
			var twitch_content_start = payload.find("CONTENT[") + 8
			var twitch_content_end = payload.find("]", twitch_content_start)
			var twitch_name_start = payload.find("NAME[") + 5
			var twitch_name_end = payload.find("]", twitch_name_start)
			var twitch_content_payload = payload.substr(twitch_content_start, twitch_content_end - twitch_content_start)
			var twitch_name_payload = payload.substr(twitch_name_start, twitch_name_end - twitch_name_start)
			print(s_i + "twitch_content_payload: " + twitch_content_payload)
			print(s_i + "twitch_name_payload: " + twitch_name_payload)
			payload_flag = false
