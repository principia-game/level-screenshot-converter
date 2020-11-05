# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
	raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Plvl(KaitaiStruct):

	class LevelVersion(Enum):
		any = 0
		version_beta_1 = 1
		version_beta_2 = 2
		version_beta_3 = 3
		version_beta_4 = 4
		version_beta_5 = 5
		version_beta_6 = 6
		version_beta_7 = 7
		version_beta_8 = 8
		version_beta_9 = 9
		version_beta_10 = 10
		version_beta_11 = 11
		version_beta_12 = 12
		version_beta_13 = 13
		version_beta_14 = 14
		version_1_0 = 15
		version_1_1_6 = 16
		version_1_1_7 = 17
		version_1_2 = 18
		version_1_2_1 = 19
		version_1_2_2 = 20
		version_1_2_3 = 21
		version_1_2_4 = 22
		version_1_3_0_1 = 23
		version_1_3_0_2 = 24
		version_1_3_0_3 = 25
		version_1_4 = 26
		version_1_4_0_2 = 27
		version_1_5 = 28
		version_1_5_1 = 29

	class LevelType(Enum):
		puzzle = 0
		adventure = 1
		creative = 2
	def __init__(self, _io, _parent=None, _root=None):
		self._io = _io
		self._parent = _parent
		self._root = _root if _root else self
		self._read()

	def _read(self):
		self.version = self._io.read_u1()
		self.type = self._root.LevelType(self._io.read_u1())
		self.community_id = self._io.read_u4le()
		if self.version >= 28:
			self.autosave_id = self._io.read_u4le()

		self.revision = self._io.read_u4le()
		self.parent_id = self._io.read_u4le()
		self.name_size = self._io.read_u1()
		self.descr_size = self._io.read_u2le()
		self.allow_derivatives = self._io.read_u1()
		if self.version >= 3:
			self.visibility = self._io.read_u1()

		if self.version >= 7:
			self.parent_revision = self._io.read_u4le()

		if self.version >= 7:
			self.pause_on_finish = self._io.read_u1()

		if self.version >= 7:
			self.show_score = self._io.read_u1()

		self.bg = self._io.read_u1()
		if self.version >= 28:
			self.bg_color = self._io.read_u4le()

		self.size_x = self._io.read_u2le()
		self.size_y = self._io.read_u2le()
		if self.version >= 12:
			self.size_x_2 = self._io.read_u2le()

		if self.version >= 12:
			self.size_y_2 = self._io.read_u2le()

		self.velocity_iterations = self._io.read_u1()
		self.position_iterations = self._io.read_u1()
		self.final_score = self._io.read_u4le()
		self.sandbox_cam_x = self._io.read_f4le()
		self.sandbox_cam_y = self._io.read_f4le()
		self.sandbox_cam_zoom = self._io.read_f4le()
		if self.version >= 3:
			self.gravity_x = self._io.read_f4le()

		if self.version >= 3:
			self.gravity_y = self._io.read_f4le()

		if self.version >= 13:
			self.bounds_x1 = self._io.read_f4le()

		if self.version >= 13:
			self.bounds_y1 = self._io.read_f4le()

		if self.version >= 13:
			self.bounds_x2 = self._io.read_f4le()

		if self.version >= 13:
			self.bounds_y2 = self._io.read_f4le()

		if self.version >= 9:
			self.flags = self._io.read_u8le()

		if self.version >= 26:
			self.prismatic_tolerance = self._io.read_f4le()

		if self.version >= 26:
			self.pivot_tolerance = self._io.read_f4le()

		if self.version >= 28:
			self.seed = self._io.read_u8le()

		if self.version >= 28:
			self.adventure_id = self._io.read_u4le()

		if self.version >= 28:
			self.linear_damping = self._io.read_f4le()

		if self.version >= 28:
			self.angular_damping = self._io.read_f4le()

		if self.version >= 28:
			self.joint_friction = self._io.read_f4le()

		if self.version >= 28:
			self.body_absorb_time = self._io.read_f4le()

		if self.version >= 28:
			self.respawn_cooldown = self._io.read_f4le()

		if self.version >= 28:
			self.compression_buf_size = self._io.read_u8le()

		self.name = (self._io.read_bytes(self.name_size)).decode(u"UTF-8")
		if self.version >= 6:
			self.unknown_header = self._io.read_bytes((128 * 128))

		self.descr = (self._io.read_bytes(self.descr_size)).decode(u"UTF-8")
		if self.version < 28:
			self.group_count_pre28 = self._io.read_u2le()

		if self.version < 28:
			self.entity_count_pre28 = self._io.read_u2le()

		if self.version < 28:
			self.connection_count_pre28 = self._io.read_u2le()

		if self.version < 28:
			self.cable_count_pre28 = self._io.read_u2le()

		if self.version >= 28:
			self.group_count = self._io.read_u4le()

		if self.version >= 28:
			self.entity_count = self._io.read_u4le()

		if self.version >= 28:
			self.connection_count = self._io.read_u4le()

		if self.version >= 28:
			self.cable_count = self._io.read_u4le()

		if self.version >= 28:
			self.chunk_count = self._io.read_u4le()

		if self.version >= 28:
			self.state_size = self._io.read_u4le()

		if self.version >= 28:
			self.gencount = self._io.read_u4le()

		self.level_buffer = self._io.read_bytes_full()


