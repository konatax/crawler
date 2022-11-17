var window = global;
var navigator = {
    "appName": "Netscape"
}
!function(a, b) {
    "function" == typeof define && define.amd ? define(["exports"], b) : b("object" == typeof exports && "string" != typeof exports.nodeName ? module.exports : a)
}(this, function(a) {
    function e(a, b, c) {
        null != a && ("number" == typeof a ? this.fromNumber(a, b, c) : null == b && "string" != typeof a ? this.fromString(a, 256) : this.fromString(a, b))
    }
    function f() {
        return new e(null)
    }
    function g(a, b, c, d, e, f) {
        for (; --f >= 0; ) {
            var g = b * this[a++] + c[d] + e;
            e = Math.floor(g / 67108864),
            c[d++] = 67108863 & g
        }
        return e
    }
    function h(a, b, c, d, e, f) {
        for (var g = 32767 & b, h = b >> 15; --f >= 0; ) {
            var i = 32767 & this[a]
              , j = this[a++] >> 15
              , k = h * i + j * g;
            i = g * i + ((32767 & k) << 15) + c[d] + (1073741823 & e),
            e = (i >>> 30) + (k >>> 15) + h * j + (e >>> 30),
            c[d++] = 1073741823 & i
        }
        return e
    }
    function i(a, b, c, d, e, f) {
        for (var g = 16383 & b, h = b >> 14; --f >= 0; ) {
            var i = 16383 & this[a]
              , j = this[a++] >> 14
              , k = h * i + j * g;
            i = g * i + ((16383 & k) << 14) + c[d] + e,
            e = (i >> 28) + (k >> 14) + h * j,
            c[d++] = 268435455 & i
        }
        return e
    }
    function o(a) {
        return k.charAt(a)
    }
    function p(a, b) {
        var c = l[a.charCodeAt(b)];
        return null == c ? -1 : c
    }
    function q(a) {
        for (var b = this.t - 1; b >= 0; --b)
            a[b] = this[b];
        a.t = this.t,
        a.s = this.s
    }
    function r(a) {
        this.t = 1,
        this.s = 0 > a ? -1 : 0,
        a > 0 ? this[0] = a : -1 > a ? this[0] = a + this.DV : this.t = 0
    }
    function s(a) {
        var b = f();
        return b.fromInt(a),
        b
    }
    function t(a, b) {
        var c;
        if (16 == b)
            c = 4;
        else if (8 == b)
            c = 3;
        else if (256 == b)
            c = 8;
        else if (2 == b)
            c = 1;
        else if (32 == b)
            c = 5;
        else {
            if (4 != b)
                return void this.fromRadix(a, b);
            c = 2
        }
        this.t = 0,
        this.s = 0;
        for (var d = a.length, f = !1, g = 0; --d >= 0; ) {
            var h = 8 == c ? 255 & a[d] : p(a, d);
            0 > h ? "-" == a.charAt(d) && (f = !0) : (f = !1,
            0 == g ? this[this.t++] = h : g + c > this.DB ? (this[this.t - 1] |= (h & (1 << this.DB - g) - 1) << g,
            this[this.t++] = h >> this.DB - g) : this[this.t - 1] |= h << g,
            g += c,
            g >= this.DB && (g -= this.DB))
        }
        8 == c && 0 != (128 & a[0]) && (this.s = -1,
        g > 0 && (this[this.t - 1] |= (1 << this.DB - g) - 1 << g)),
        this.clamp(),
        f && e.ZERO.subTo(this, this)
    }
    function u() {
        for (var a = this.s & this.DM; this.t > 0 && this[this.t - 1] == a; )
            --this.t
    }
    function w(a) {
        if (this.s < 0)
            return "-" + this.negate().toString(a);
        var b;
        if (16 == a)
            b = 4;
        else if (8 == a)
            b = 3;
        else if (2 == a)
            b = 1;
        else if (32 == a)
            b = 5;
        else {
            if (4 != a)
                return this.toRadix(a);
            b = 2
        }
        var d, c = (1 << b) - 1, e = !1, f = "", g = this.t, h = this.DB - g * this.DB % b;
        if (g-- > 0)
            for (h < this.DB && (d = this[g] >> h) > 0 && (e = !0,
            f = o(d)); g >= 0; )
                b > h ? (d = (this[g] & (1 << h) - 1) << b - h,
                d |= this[--g] >> (h += this.DB - b)) : (d = this[g] >> (h -= b) & c,
                0 >= h && (h += this.DB,
                --g)),
                d > 0 && (e = !0),
                e && (f += o(d));
        return e ? f : "0"
    }
    function x() {
        var a = f();
        return e.ZERO.subTo(this, a),
        a
    }
    function y() {
        return this.s < 0 ? this.negate() : this
    }
    function z(a) {
        var b = this.s - a.s;
        if (0 != b)
            return b;
        var c = this.t;
        if (b = c - a.t,
        0 != b)
            return this.s < 0 ? -b : b;
        for (; --c >= 0; )
            if (0 != (b = this[c] - a[c]))
                return b;
        return 0
    }
    function A(a) {
        var c, b = 1;
        return 0 != (c = a >>> 16) && (a = c,
        b += 16),
        0 != (c = a >> 8) && (a = c,
        b += 8),
        0 != (c = a >> 4) && (a = c,
        b += 4),
        0 != (c = a >> 2) && (a = c,
        b += 2),
        0 != (c = a >> 1) && (a = c,
        b += 1),
        b
    }
    function B() {
        return this.t <= 0 ? 0 : this.DB * (this.t - 1) + A(this[this.t - 1] ^ this.s & this.DM)
    }
    function C(a, b) {
        var c;
        for (c = this.t - 1; c >= 0; --c)
            b[c + a] = this[c];
        for (c = a - 1; c >= 0; --c)
            b[c] = 0;
        b.t = this.t + a,
        b.s = this.s
    }
    function D(a, b) {
        for (var c = a; c < this.t; ++c)
            b[c - a] = this[c];
        b.t = Math.max(this.t - a, 0),
        b.s = this.s
    }
    function E(a, b) {
        var h, c = a % this.DB, d = this.DB - c, e = (1 << d) - 1, f = Math.floor(a / this.DB), g = this.s << c & this.DM;
        for (h = this.t - 1; h >= 0; --h)
            b[h + f + 1] = this[h] >> d | g,
            g = (this[h] & e) << c;
        for (h = f - 1; h >= 0; --h)
            b[h] = 0;
        b[f] = g,
        b.t = this.t + f + 1,
        b.s = this.s,
        b.clamp()
    }
    function F(a, b) {
        b.s = this.s;
        var c = Math.floor(a / this.DB);
        if (c >= this.t)
            return void (b.t = 0);
        var d = a % this.DB
          , e = this.DB - d
          , f = (1 << d) - 1;
        b[0] = this[c] >> d;
        for (var g = c + 1; g < this.t; ++g)
            b[g - c - 1] |= (this[g] & f) << e,
            b[g - c] = this[g] >> d;
        d > 0 && (b[this.t - c - 1] |= (this.s & f) << e),
        b.t = this.t - c,
        b.clamp()
    }
    function G(a, b) {
        for (var c = 0, d = 0, e = Math.min(a.t, this.t); e > c; )
            d += this[c] - a[c],
            b[c++] = d & this.DM,
            d >>= this.DB;
        if (a.t < this.t) {
            for (d -= a.s; c < this.t; )
                d += this[c],
                b[c++] = d & this.DM,
                d >>= this.DB;
            d += this.s
        } else {
            for (d += this.s; c < a.t; )
                d -= a[c],
                b[c++] = d & this.DM,
                d >>= this.DB;
            d -= a.s
        }
        b.s = 0 > d ? -1 : 0,
        -1 > d ? b[c++] = this.DV + d : d > 0 && (b[c++] = d),
        b.t = c,
        b.clamp()
    }
    function H(a, b) {
        var c = this.abs()
          , d = a.abs()
          , f = c.t;
        for (b.t = f + d.t; --f >= 0; )
            b[f] = 0;
        for (f = 0; f < d.t; ++f)
            b[f + c.t] = c.am(0, d[f], b, f, 0, c.t);
        b.s = 0,
        b.clamp(),
        this.s != a.s && e.ZERO.subTo(b, b)
    }
    function I(a) {
        for (var b = this.abs(), c = a.t = 2 * b.t; --c >= 0; )
            a[c] = 0;
        for (c = 0; c < b.t - 1; ++c) {
            var d = b.am(c, b[c], a, 2 * c, 0, 1);
            (a[c + b.t] += b.am(c + 1, 2 * b[c], a, 2 * c + 1, d, b.t - c - 1)) >= b.DV && (a[c + b.t] -= b.DV,
            a[c + b.t + 1] = 1)
        }
        a.t > 0 && (a[a.t - 1] += b.am(c, b[c], a, 2 * c, 0, 1)),
        a.s = 0,
        a.clamp()
    }
    function J(a, b, c) {
        var d = a.abs();
        if (!(d.t <= 0)) {
            var g = this.abs();
            if (g.t < d.t)
                return null != b && b.fromInt(0),
                void (null != c && this.copyTo(c));
            null == c && (c = f());
            var h = f()
              , i = this.s
              , j = a.s
              , k = this.DB - A(d[d.t - 1]);
            k > 0 ? (d.lShiftTo(k, h),
            g.lShiftTo(k, c)) : (d.copyTo(h),
            g.copyTo(c));
            var l = h.t
              , m = h[l - 1];
            if (0 != m) {
                var n = m * (1 << this.F1) + (l > 1 ? h[l - 2] >> this.F2 : 0)
                  , o = this.FV / n
                  , p = (1 << this.F1) / n
                  , q = 1 << this.F2
                  , r = c.t
                  , s = r - l
                  , t = null == b ? f() : b;
                for (h.dlShiftTo(s, t),
                c.compareTo(t) >= 0 && (c[c.t++] = 1,
                c.subTo(t, c)),
                e.ONE.dlShiftTo(l, t),
                t.subTo(h, h); h.t < l; )
                    h[h.t++] = 0;
                for (; --s >= 0; ) {
                    var u = c[--r] == m ? this.DM : Math.floor(c[r] * o + (c[r - 1] + q) * p);
                    if ((c[r] += h.am(0, u, c, s, 0, l)) < u)
                        for (h.dlShiftTo(s, t),
                        c.subTo(t, c); c[r] < --u; )
                            c.subTo(t, c)
                }
                null != b && (c.drShiftTo(l, b),
                i != j && e.ZERO.subTo(b, b)),
                c.t = l,
                c.clamp(),
                k > 0 && c.rShiftTo(k, c),
                0 > i && e.ZERO.subTo(c, c)
            }
        }
    }
    function K(a) {
        var b = f();
        return this.abs().divRemTo(a, null, b),
        this.s < 0 && b.compareTo(e.ZERO) > 0 && a.subTo(b, b),
        b
    }
    function L(a) {
        this.m = a
    }
    function M(a) {
        return a.s < 0 || a.compareTo(this.m) >= 0 ? a.mod(this.m) : a
    }
    function N(a) {
        return a
    }
    function O(a) {
        a.divRemTo(this.m, null, a)
    }
    function P(a, b, c) {
        a.multiplyTo(b, c),
        this.reduce(c)
    }
    function Q(a, b) {
        a.squareTo(b),
        this.reduce(b)
    }
    function R() {
        if (this.t < 1)
            return 0;
        var a = this[0];
        if (0 == (1 & a))
            return 0;
        var b = 3 & a;
        return b = b * (2 - (15 & a) * b) & 15,
        b = b * (2 - (255 & a) * b) & 255,
        b = b * (2 - ((65535 & a) * b & 65535)) & 65535,
        b = b * (2 - a * b % this.DV) % this.DV,
        b > 0 ? this.DV - b : -b
    }
    function S(a) {
        this.m = a,
        this.mp = a.invDigit(),
        this.mpl = 32767 & this.mp,
        this.mph = this.mp >> 15,
        this.um = (1 << a.DB - 15) - 1,
        this.mt2 = 2 * a.t
    }
    function T(a) {
        var b = f();
        return a.abs().dlShiftTo(this.m.t, b),
        b.divRemTo(this.m, null, b),
        a.s < 0 && b.compareTo(e.ZERO) > 0 && this.m.subTo(b, b),
        b
    }
    function U(a) {
        var b = f();
        return a.copyTo(b),
        this.reduce(b),
        b
    }
    function V(a) {
        for (; a.t <= this.mt2; )
            a[a.t++] = 0;
        for (var b = 0; b < this.m.t; ++b) {
            var c = 32767 & a[b]
              , d = c * this.mpl + ((c * this.mph + (a[b] >> 15) * this.mpl & this.um) << 15) & a.DM;
            for (c = b + this.m.t,
            a[c] += this.m.am(0, d, a, b, 0, this.m.t); a[c] >= a.DV; )
                a[c] -= a.DV,
                a[++c]++
        }
        a.clamp(),
        a.drShiftTo(this.m.t, a),
        a.compareTo(this.m) >= 0 && a.subTo(this.m, a)
    }
    function W(a, b) {
        a.squareTo(b),
        this.reduce(b)
    }
    function X(a, b, c) {
        a.multiplyTo(b, c),
        this.reduce(c)
    }
    function Y() {
        return 0 == (this.t > 0 ? 1 & this[0] : this.s)
    }
    function Z(a, b) {
        if (a > 4294967295 || 1 > a)
            return e.ONE;
        var c = f()
          , d = f()
          , g = b.convert(this)
          , h = A(a) - 1;
        for (g.copyTo(c); --h >= 0; )
            if (b.sqrTo(c, d),
            (a & 1 << h) > 0)
                b.mulTo(d, g, c);
            else {
                var i = c;
                c = d,
                d = i
            }
        return b.revert(c)
    }
    function $(a, b) {
        var c;
        return c = 256 > a || b.isEven() ? new L(b) : new S(b),
        this.exp(a, c)
    }
    function _() {
        var a = f();
        return this.copyTo(a),
        a
    }
    function aa() {
        if (this.s < 0) {
            if (1 == this.t)
                return this[0] - this.DV;
            if (0 == this.t)
                return -1
        } else {
            if (1 == this.t)
                return this[0];
            if (0 == this.t)
                return 0
        }
        return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
    }
    function ba() {
        return 0 == this.t ? this.s : this[0] << 24 >> 24
    }
    function ca() {
        return 0 == this.t ? this.s : this[0] << 16 >> 16
    }
    function da(a) {
        return Math.floor(Math.LN2 * this.DB / Math.log(a))
    }
    function ea() {
        return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
    }
    function fa(a) {
        if (null == a && (a = 10),
        0 == this.signum() || 2 > a || a > 36)
            return "0";
        var b = this.chunkSize(a)
          , c = Math.pow(a, b)
          , d = s(c)
          , e = f()
          , g = f()
          , h = "";
        for (this.divRemTo(d, e, g); e.signum() > 0; )
            h = (c + g.intValue()).toString(a).substr(1) + h,
            e.divRemTo(d, e, g);
        return g.intValue().toString(a) + h
    }
    function ga(a, b) {
        this.fromInt(0),
        null == b && (b = 10);
        for (var c = this.chunkSize(b), d = Math.pow(b, c), f = !1, g = 0, h = 0, i = 0; i < a.length; ++i) {
            var j = p(a, i);
            0 > j ? "-" == a.charAt(i) && 0 == this.signum() && (f = !0) : (h = b * h + j,
            ++g >= c && (this.dMultiply(d),
            this.dAddOffset(h, 0),
            g = 0,
            h = 0))
        }
        g > 0 && (this.dMultiply(Math.pow(b, g)),
        this.dAddOffset(h, 0)),
        f && e.ZERO.subTo(this, this)
    }
    function ha(a, b, c) {
        if ("number" == typeof b)
            if (2 > a)
                this.fromInt(1);
            else
                for (this.fromNumber(a, c),
                this.testBit(a - 1) || this.bitwiseTo(e.ONE.shiftLeft(a - 1), pa, this),
                this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(b); )
                    this.dAddOffset(2, 0),
                    this.bitLength() > a && this.subTo(e.ONE.shiftLeft(a - 1), this);
        else {
            var d = new Array
              , f = 7 & a;
            d.length = (a >> 3) + 1,
            b.nextBytes(d),
            f > 0 ? d[0] &= (1 << f) - 1 : d[0] = 0,
            this.fromString(d, 256)
        }
    }
    function ia() {
        var a = this.t
          , b = new Array;
        b[0] = this.s;
        var d, c = this.DB - a * this.DB % 8, e = 0;
        if (a-- > 0)
            for (c < this.DB && (d = this[a] >> c) != (this.s & this.DM) >> c && (b[e++] = d | this.s << this.DB - c); a >= 0; )
                8 > c ? (d = (this[a] & (1 << c) - 1) << 8 - c,
                d |= this[--a] >> (c += this.DB - 8)) : (d = this[a] >> (c -= 8) & 255,
                0 >= c && (c += this.DB,
                --a)),
                0 != (128 & d) && (d |= -256),
                0 == e && (128 & this.s) != (128 & d) && ++e,
                (e > 0 || d != this.s) && (b[e++] = d);
        return b
    }
    function ja(a) {
        return 0 == this.compareTo(a)
    }
    function ka(a) {
        return this.compareTo(a) < 0 ? this : a
    }
    function la(a) {
        return this.compareTo(a) > 0 ? this : a
    }
    function ma(a, b, c) {
        var d, e, f = Math.min(a.t, this.t);
        for (d = 0; f > d; ++d)
            c[d] = b(this[d], a[d]);
        if (a.t < this.t) {
            for (e = a.s & this.DM,
            d = f; d < this.t; ++d)
                c[d] = b(this[d], e);
            c.t = this.t
        } else {
            for (e = this.s & this.DM,
            d = f; d < a.t; ++d)
                c[d] = b(e, a[d]);
            c.t = a.t
        }
        c.s = b(this.s, a.s),
        c.clamp()
    }
    function na(a, b) {
        return a & b
    }
    function oa(a) {
        var b = f();
        return this.bitwiseTo(a, na, b),
        b
    }
    function pa(a, b) {
        return a | b
    }
    function qa(a) {
        var b = f();
        return this.bitwiseTo(a, pa, b),
        b
    }
    function ra(a, b) {
        return a ^ b
    }
    function sa(a) {
        var b = f();
        return this.bitwiseTo(a, ra, b),
        b
    }
    function ta(a, b) {
        return a & ~b
    }
    function ua(a) {
        var b = f();
        return this.bitwiseTo(a, ta, b),
        b
    }
    function va() {
        for (var a = f(), b = 0; b < this.t; ++b)
            a[b] = this.DM & ~this[b];
        return a.t = this.t,
        a.s = ~this.s,
        a
    }
    function wa(a) {
        var b = f();
        return 0 > a ? this.rShiftTo(-a, b) : this.lShiftTo(a, b),
        b
    }
    function xa(a) {
        var b = f();
        return 0 > a ? this.lShiftTo(-a, b) : this.rShiftTo(a, b),
        b
    }
    function ya(a) {
        if (0 == a)
            return -1;
        var b = 0;
        return 0 == (65535 & a) && (a >>= 16,
        b += 16),
        0 == (255 & a) && (a >>= 8,
        b += 8),
        0 == (15 & a) && (a >>= 4,
        b += 4),
        0 == (3 & a) && (a >>= 2,
        b += 2),
        0 == (1 & a) && ++b,
        b
    }
    function za() {
        for (var a = 0; a < this.t; ++a)
            if (0 != this[a])
                return a * this.DB + ya(this[a]);
        return this.s < 0 ? this.t * this.DB : -1
    }
    function Aa(a) {
        for (var b = 0; 0 != a; )
            a &= a - 1,
            ++b;
        return b
    }
    function Ba() {
        for (var a = 0, b = this.s & this.DM, c = 0; c < this.t; ++c)
            a += Aa(this[c] ^ b);
        return a
    }
    function Ca(a) {
        var b = Math.floor(a / this.DB);
        return b >= this.t ? 0 != this.s : 0 != (this[b] & 1 << a % this.DB)
    }
    function Da(a, b) {
        var c = e.ONE.shiftLeft(a);
        return this.bitwiseTo(c, b, c),
        c
    }
    function Ea(a) {
        return this.changeBit(a, pa)
    }
    function Fa(a) {
        return this.changeBit(a, ta)
    }
    function Ga(a) {
        return this.changeBit(a, ra)
    }
    function Ha(a, b) {
        for (var c = 0, d = 0, e = Math.min(a.t, this.t); e > c; )
            d += this[c] + a[c],
            b[c++] = d & this.DM,
            d >>= this.DB;
        if (a.t < this.t) {
            for (d += a.s; c < this.t; )
                d += this[c],
                b[c++] = d & this.DM,
                d >>= this.DB;
            d += this.s
        } else {
            for (d += this.s; c < a.t; )
                d += a[c],
                b[c++] = d & this.DM,
                d >>= this.DB;
            d += a.s
        }
        b.s = 0 > d ? -1 : 0,
        d > 0 ? b[c++] = d : -1 > d && (b[c++] = this.DV + d),
        b.t = c,
        b.clamp()
    }
    function Ia(a) {
        var b = f();
        return this.addTo(a, b),
        b
    }
    function Ja(a) {
        var b = f();
        return this.subTo(a, b),
        b
    }
    function Ka(a) {
        var b = f();
        return this.multiplyTo(a, b),
        b
    }
    function La() {
        var a = f();
        return this.squareTo(a),
        a
    }
    function Ma(a) {
        var b = f();
        return this.divRemTo(a, b, null),
        b
    }
    function Na(a) {
        var b = f();
        return this.divRemTo(a, null, b),
        b
    }
    function Oa(a) {
        var b = f()
          , c = f();
        return this.divRemTo(a, b, c),
        new Array(b,c)
    }
    function Pa(a) {
        this[this.t] = this.am(0, a - 1, this, 0, 0, this.t),
        ++this.t,
        this.clamp()
    }
    function Qa(a, b) {
        if (0 != a) {
            for (; this.t <= b; )
                this[this.t++] = 0;
            for (this[b] += a; this[b] >= this.DV; )
                this[b] -= this.DV,
                ++b >= this.t && (this[this.t++] = 0),
                ++this[b]
        }
    }
    function Ra() {}
    function Sa(a) {
        return a
    }
    function Ta(a, b, c) {
        a.multiplyTo(b, c)
    }
    function Ua(a, b) {
        a.squareTo(b)
    }
    function Va(a) {
        return this.exp(a, new Ra)
    }
    function Wa(a, b, c) {
        var d = Math.min(this.t + a.t, b);
        for (c.s = 0,
        c.t = d; d > 0; )
            c[--d] = 0;
        var e;
        for (e = c.t - this.t; e > d; ++d)
            c[d + this.t] = this.am(0, a[d], c, d, 0, this.t);
        for (e = Math.min(a.t, b); e > d; ++d)
            this.am(0, a[d], c, d, 0, b - d);
        c.clamp()
    }
    function Xa(a, b, c) {
        --b;
        var d = c.t = this.t + a.t - b;
        for (c.s = 0; --d >= 0; )
            c[d] = 0;
        for (d = Math.max(b - this.t, 0); d < a.t; ++d)
            c[this.t + d - b] = this.am(b - d, a[d], c, 0, 0, this.t + d - b);
        c.clamp(),
        c.drShiftTo(1, c)
    }
    function Ya(a) {
        this.r2 = f(),
        this.q3 = f(),
        e.ONE.dlShiftTo(2 * a.t, this.r2),
        this.mu = this.r2.divide(a),
        this.m = a
    }
    function Za(a) {
        if (a.s < 0 || a.t > 2 * this.m.t)
            return a.mod(this.m);
        if (a.compareTo(this.m) < 0)
            return a;
        var b = f();
        return a.copyTo(b),
        this.reduce(b),
        b
    }
    function $a(a) {
        return a
    }
    function _a(a) {
        for (a.drShiftTo(this.m.t - 1, this.r2),
        a.t > this.m.t + 1 && (a.t = this.m.t + 1,
        a.clamp()),
        this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
        this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); a.compareTo(this.r2) < 0; )
            a.dAddOffset(1, this.m.t + 1);
        for (a.subTo(this.r2, a); a.compareTo(this.m) >= 0; )
            a.subTo(this.m, a)
    }
    function ab(a, b) {
        a.squareTo(b),
        this.reduce(b)
    }
    function bb(a, b, c) {
        a.multiplyTo(b, c),
        this.reduce(c)
    }
    function cb(a, b) {
        var d, g, c = a.bitLength(), e = s(1);
        if (0 >= c)
            return e;
        d = 18 > c ? 1 : 48 > c ? 3 : 144 > c ? 4 : 768 > c ? 5 : 6,
        g = 8 > c ? new L(b) : b.isEven() ? new Ya(b) : new S(b);
        var h = new Array
          , i = 3
          , j = d - 1
          , k = (1 << d) - 1;
        if (h[1] = g.convert(this),
        d > 1) {
            var l = f();
            for (g.sqrTo(h[1], l); k >= i; )
                h[i] = f(),
                g.mulTo(l, h[i - 2], h[i]),
                i += 2
        }
        var n, q, m = a.t - 1, o = !0, p = f();
        for (c = A(a[m]) - 1; m >= 0; ) {
            for (c >= j ? n = a[m] >> c - j & k : (n = (a[m] & (1 << c + 1) - 1) << j - c,
            m > 0 && (n |= a[m - 1] >> this.DB + c - j)),
            i = d; 0 == (1 & n); )
                n >>= 1,
                --i;
            if ((c -= i) < 0 && (c += this.DB,
            --m),
            o)
                h[n].copyTo(e),
                o = !1;
            else {
                for (; i > 1; )
                    g.sqrTo(e, p),
                    g.sqrTo(p, e),
                    i -= 2;
                i > 0 ? g.sqrTo(e, p) : (q = e,
                e = p,
                p = q),
                g.mulTo(p, h[n], e)
            }
            for (; m >= 0 && 0 == (a[m] & 1 << c); )
                g.sqrTo(e, p),
                q = e,
                e = p,
                p = q,
                --c < 0 && (c = this.DB - 1,
                --m)
        }
        return g.revert(e)
    }
    function db(a) {
        var b = this.s < 0 ? this.negate() : this.clone()
          , c = a.s < 0 ? a.negate() : a.clone();
        if (b.compareTo(c) < 0) {
            var d = b;
            b = c,
            c = d
        }
        var e = b.getLowestSetBit()
          , f = c.getLowestSetBit();
        if (0 > f)
            return b;
        for (f > e && (f = e),
        f > 0 && (b.rShiftTo(f, b),
        c.rShiftTo(f, c)); b.signum() > 0; )
            (e = b.getLowestSetBit()) > 0 && b.rShiftTo(e, b),
            (e = c.getLowestSetBit()) > 0 && c.rShiftTo(e, c),
            b.compareTo(c) >= 0 ? (b.subTo(c, b),
            b.rShiftTo(1, b)) : (c.subTo(b, c),
            c.rShiftTo(1, c));
        return f > 0 && c.lShiftTo(f, c),
        c
    }
    function eb(a) {
        if (0 >= a)
            return 0;
        var b = this.DV % a
          , c = this.s < 0 ? a - 1 : 0;
        if (this.t > 0)
            if (0 == b)
                c = this[0] % a;
            else
                for (var d = this.t - 1; d >= 0; --d)
                    c = (b * c + this[d]) % a;
        return c
    }
    function fb(a) {
        var b = a.isEven();
        if (this.isEven() && b || 0 == a.signum())
            return e.ZERO;
        for (var c = a.clone(), d = this.clone(), f = s(1), g = s(0), h = s(0), i = s(1); 0 != c.signum(); ) {
            for (; c.isEven(); )
                c.rShiftTo(1, c),
                b ? (f.isEven() && g.isEven() || (f.addTo(this, f),
                g.subTo(a, g)),
                f.rShiftTo(1, f)) : g.isEven() || g.subTo(a, g),
                g.rShiftTo(1, g);
            for (; d.isEven(); )
                d.rShiftTo(1, d),
                b ? (h.isEven() && i.isEven() || (h.addTo(this, h),
                i.subTo(a, i)),
                h.rShiftTo(1, h)) : i.isEven() || i.subTo(a, i),
                i.rShiftTo(1, i);
            c.compareTo(d) >= 0 ? (c.subTo(d, c),
            b && f.subTo(h, f),
            g.subTo(i, g)) : (d.subTo(c, d),
            b && h.subTo(f, h),
            i.subTo(g, i))
        }
        return 0 != d.compareTo(e.ONE) ? e.ZERO : i.compareTo(a) >= 0 ? i.subtract(a) : i.signum() < 0 ? (i.addTo(a, i),
        i.signum() < 0 ? i.add(a) : i) : i
    }
    function ib(a) {
        var b, c = this.abs();
        if (1 == c.t && c[0] <= gb[gb.length - 1]) {
            for (b = 0; b < gb.length; ++b)
                if (c[0] == gb[b])
                    return !0;
            return !1
        }
        if (c.isEven())
            return !1;
        for (b = 1; b < gb.length; ) {
            for (var d = gb[b], e = b + 1; e < gb.length && hb > d; )
                d *= gb[e++];
            for (d = c.modInt(d); e > b; )
                if (d % gb[b++] == 0)
                    return !1
        }
        return c.millerRabin(a)
    }
    function jb(a) {
        var b = this.subtract(e.ONE)
          , c = b.getLowestSetBit();
        if (0 >= c)
            return !1;
        var d = b.shiftRight(c);
        a = a + 1 >> 1,
        a > gb.length && (a = gb.length);
        for (var g = f(), h = 0; a > h; ++h) {
            g.fromInt(gb[Math.floor(Math.random() * gb.length)]);
            var i = g.modPow(d, this);
            if (0 != i.compareTo(e.ONE) && 0 != i.compareTo(b)) {
                for (var j = 1; j++ < c && 0 != i.compareTo(b); )
                    if (i = i.modPowInt(2, this),
                    0 == i.compareTo(e.ONE))
                        return !1;
                if (0 != i.compareTo(b))
                    return !1
            }
        }
        return !0
    }
    function kb() {
        this.i = 0,
        this.j = 0,
        this.S = new Array
    }
    function lb(a) {
        var b, c, d;
        for (b = 0; 256 > b; ++b)
            this.S[b] = b;
        for (c = 0,
        b = 0; 256 > b; ++b)
            c = c + this.S[b] + a[b % a.length] & 255,
            d = this.S[b],
            this.S[b] = this.S[c],
            this.S[c] = d;
        this.i = 0,
        this.j = 0
    }
    function mb() {
        var a;
        return this.i = this.i + 1 & 255,
        this.j = this.j + this.S[this.i] & 255,
        a = this.S[this.i],
        this.S[this.i] = this.S[this.j],
        this.S[this.j] = a,
        this.S[a + this.S[this.i] & 255]
    }
    function nb() {
        return new kb
    }
    function vb() {
        if (null == pb) {
            for (pb = nb(); ob > rb; ) {
                var a = Math.floor(65536 * Math.random());
                qb[rb++] = 255 & a
            }
            for (pb.init(qb),
            rb = 0; rb < qb.length; ++rb)
                qb[rb] = 0;
            rb = 0
        }
        return pb.next()
    }
    function wb(a) {
        var b;
        for (b = 0; b < a.length; ++b)
            a[b] = vb()
    }
    function xb() {}
    function yb(a, b) {
        return new e(a,b)
    }
    function Bb(a, b) {
        if (b < a.length + 11)
            return console.error("Message too long for RSA"),
            null;
        for (var c = new Array, d = a.length - 1; d >= 0 && b > 0; ) {
            var f = a.charCodeAt(d--);
            128 > f ? c[--b] = f : f > 127 && 2048 > f ? (c[--b] = 63 & f | 128,
            c[--b] = f >> 6 | 192) : (c[--b] = 63 & f | 128,
            c[--b] = f >> 6 & 63 | 128,
            c[--b] = f >> 12 | 224)
        }
        c[--b] = 0;
        for (var g = new xb, h = new Array; b > 2; ) {
            for (h[0] = 0; 0 == h[0]; )
                g.nextBytes(h);
            c[--b] = h[0]
        }
        return c[--b] = 2,
        c[--b] = 0,
        new e(c)
    }
    function Cb() {
        this.n = null,
        this.e = 0,
        this.d = null,
        this.p = null,
        this.q = null,
        this.dmp1 = null,
        this.dmq1 = null,
        this.coeff = null
    }
    function Db(a, b) {
        null != a && null != b && a.length > 0 && b.length > 0 ? (this.n = yb(a, 16),
        this.e = parseInt(b, 16)) : console.error("Invalid RSA public key")
    }
    function Eb(a) {
        return a.modPowInt(this.e, this.n)
    }
    function Fb(a) {
        var b = Bb(a, this.n.bitLength() + 7 >> 3);
        if (null == b)
            return null;
        var c = this.doPublic(b);
        if (null == c)
            return null;
        var d = c.toString(16);
        console.log(d);
        return 0 == (1 & d.length) ? d : "0" + d
    }
    function Gb(a, b) {
        for (var c = a.toByteArray(), d = 0; d < c.length && 0 == c[d]; )
            ++d;
        if (c.length - d != b - 1 || 2 != c[d])
            return null;
        for (++d; 0 != c[d]; )
            if (++d >= c.length)
                return null;
        for (var e = ""; ++d < c.length; ) {
            var f = 255 & c[d];
            128 > f ? e += String.fromCharCode(f) : f > 191 && 224 > f ? (e += String.fromCharCode((31 & f) << 6 | 63 & c[d + 1]),
            ++d) : (e += String.fromCharCode((15 & f) << 12 | (63 & c[d + 1]) << 6 | 63 & c[d + 2]),
            d += 2)
        }
        return e
    }
    function Hb(a, b, c) {
        null != a && null != b && a.length > 0 && b.length > 0 ? (this.n = yb(a, 16),
        this.e = parseInt(b, 16),
        this.d = yb(c, 16)) : console.error("Invalid RSA private key")
    }
    function Ib(a, b, c, d, e, f, g, h) {
        null != a && null != b && a.length > 0 && b.length > 0 ? (this.n = yb(a, 16),
        this.e = parseInt(b, 16),
        this.d = yb(c, 16),
        this.p = yb(d, 16),
        this.q = yb(e, 16),
        this.dmp1 = yb(f, 16),
        this.dmq1 = yb(g, 16),
        this.coeff = yb(h, 16)) : console.error("Invalid RSA private key")
    }
    function Jb(a, b) {
        var c = new xb
          , d = a >> 1;
        this.e = parseInt(b, 16);
        for (var f = new e(b,16); ; ) {
            for (; this.p = new e(a - d,1,c),
            0 != this.p.subtract(e.ONE).gcd(f).compareTo(e.ONE) || !this.p.isProbablePrime(10); )
                ;
            for (; this.q = new e(d,1,c),
            0 != this.q.subtract(e.ONE).gcd(f).compareTo(e.ONE) || !this.q.isProbablePrime(10); )
                ;
            if (this.p.compareTo(this.q) <= 0) {
                var g = this.p;
                this.p = this.q,
                this.q = g
            }
            var h = this.p.subtract(e.ONE)
              , i = this.q.subtract(e.ONE)
              , j = h.multiply(i);
            if (0 == j.gcd(f).compareTo(e.ONE)) {
                this.n = this.p.multiply(this.q),
                this.d = f.modInverse(j),
                this.dmp1 = this.d.mod(h),
                this.dmq1 = this.d.mod(i),
                this.coeff = this.q.modInverse(this.p);
                break
            }
        }
    }
    function Kb(a) {
        if (null == this.p || null == this.q)
            return a.modPow(this.d, this.n);
        for (var b = a.mod(this.p).modPow(this.dmp1, this.p), c = a.mod(this.q).modPow(this.dmq1, this.q); b.compareTo(c) < 0; )
            b = b.add(this.p);
        return b.subtract(c).multiply(this.coeff).mod(this.p).multiply(this.q).add(c)
    }
    function Lb(a) {
        var b = yb(a, 16)
          , c = this.doPrivate(b);
        return null == c ? null : Gb(c, this.n.bitLength() + 7 >> 3)
    }
    function Ob(a) {
        var b, c, d = "";
        for (b = 0; b + 3 <= a.length; b += 3)
            c = parseInt(a.substring(b, b + 3), 16),
            d += Mb.charAt(c >> 6) + Mb.charAt(63 & c);
        for (b + 1 == a.length ? (c = parseInt(a.substring(b, b + 1), 16),
        d += Mb.charAt(c << 2)) : b + 2 == a.length && (c = parseInt(a.substring(b, b + 2), 16),
        d += Mb.charAt(c >> 2) + Mb.charAt((3 & c) << 4)); (3 & d.length) > 0; )
            d += Nb;
        return d
    }
    function Pb(a) {
        var c, e, b = "", d = 0;
        for (c = 0; c < a.length && a.charAt(c) != Nb; ++c)
            v = Mb.indexOf(a.charAt(c)),
            v < 0 || (0 == d ? (b += o(v >> 2),
            e = 3 & v,
            d = 1) : 1 == d ? (b += o(e << 2 | v >> 4),
            e = 15 & v,
            d = 2) : 2 == d ? (b += o(e),
            b += o(v >> 2),
            e = 3 & v,
            d = 3) : (b += o(e << 2 | v >> 4),
            b += o(15 & v),
            d = 0));
        return 1 == d && (b += o(e << 2)),
        b
    }
    var b, c = 0xdeadbeefcafe, d = 15715070 == (16777215 & c);
    d && "Microsoft Internet Explorer" == navigator.appName ? (e.prototype.am = h,
    b = 30) : d && "Netscape" != navigator.appName ? (e.prototype.am = g,
    b = 26) : (e.prototype.am = i,
    b = 28),
    e.prototype.DB = b,
    e.prototype.DM = (1 << b) - 1,
    e.prototype.DV = 1 << b;
    var j = 52;
    e.prototype.FV = Math.pow(2, j),
    e.prototype.F1 = j - b,
    e.prototype.F2 = 2 * b - j;
    var m, n, k = "0123456789abcdefghijklmnopqrstuvwxyz", l = new Array;
    for (m = "0".charCodeAt(0),
    n = 0; 9 >= n; ++n)
        l[m++] = n;
    for (m = "a".charCodeAt(0),
    n = 10; 36 > n; ++n)
        l[m++] = n;
    for (m = "A".charCodeAt(0),
    n = 10; 36 > n; ++n)
        l[m++] = n;
    L.prototype.convert = M,
    L.prototype.revert = N,
    L.prototype.reduce = O,
    L.prototype.mulTo = P,
    L.prototype.sqrTo = Q,
    S.prototype.convert = T,
    S.prototype.revert = U,
    S.prototype.reduce = V,
    S.prototype.mulTo = X,
    S.prototype.sqrTo = W,
    e.prototype.copyTo = q,
    e.prototype.fromInt = r,
    e.prototype.fromString = t,
    e.prototype.clamp = u,
    e.prototype.dlShiftTo = C,
    e.prototype.drShiftTo = D,
    e.prototype.lShiftTo = E,
    e.prototype.rShiftTo = F,
    e.prototype.subTo = G,
    e.prototype.multiplyTo = H,
    e.prototype.squareTo = I,
    e.prototype.divRemTo = J,
    e.prototype.invDigit = R,
    e.prototype.isEven = Y,
    e.prototype.exp = Z,
    e.prototype.toString = w,
    e.prototype.negate = x,
    e.prototype.abs = y,
    e.prototype.compareTo = z,
    e.prototype.bitLength = B,
    e.prototype.mod = K,
    e.prototype.modPowInt = $,
    e.ZERO = s(0),
    e.ONE = s(1),
    Ra.prototype.convert = Sa,
    Ra.prototype.revert = Sa,
    Ra.prototype.mulTo = Ta,
    Ra.prototype.sqrTo = Ua,
    Ya.prototype.convert = Za,
    Ya.prototype.revert = $a,
    Ya.prototype.reduce = _a,
    Ya.prototype.mulTo = bb,
    Ya.prototype.sqrTo = ab;
    var gb = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
      , hb = (1 << 26) / gb[gb.length - 1];
    e.prototype.chunkSize = da,
    e.prototype.toRadix = fa,
    e.prototype.fromRadix = ga,
    e.prototype.fromNumber = ha,
    e.prototype.bitwiseTo = ma,
    e.prototype.changeBit = Da,
    e.prototype.addTo = Ha,
    e.prototype.dMultiply = Pa,
    e.prototype.dAddOffset = Qa,
    e.prototype.multiplyLowerTo = Wa,
    e.prototype.multiplyUpperTo = Xa,
    e.prototype.modInt = eb,
    e.prototype.millerRabin = jb,
    e.prototype.clone = _,
    e.prototype.intValue = aa,
    e.prototype.byteValue = ba,
    e.prototype.shortValue = ca,
    e.prototype.signum = ea,
    e.prototype.toByteArray = ia,
    e.prototype.equals = ja,
    e.prototype.min = ka,
    e.prototype.max = la,
    e.prototype.and = oa,
    e.prototype.or = qa,
    e.prototype.xor = sa,
    e.prototype.andNot = ua,
    e.prototype.not = va,
    e.prototype.shiftLeft = wa,
    e.prototype.shiftRight = xa,
    e.prototype.getLowestSetBit = za,
    e.prototype.bitCount = Ba,
    e.prototype.testBit = Ca,
    e.prototype.setBit = Ea,
    e.prototype.clearBit = Fa,
    e.prototype.flipBit = Ga,
    e.prototype.add = Ia,
    e.prototype.subtract = Ja,
    e.prototype.multiply = Ka,
    e.prototype.divide = Ma,
    e.prototype.remainder = Na,
    e.prototype.divideAndRemainder = Oa,
    e.prototype.modPow = cb,
    e.prototype.modInverse = fb,
    e.prototype.pow = Va,
    e.prototype.gcd = db,
    e.prototype.isProbablePrime = ib,
    e.prototype.square = La,
    kb.prototype.init = lb,
    kb.prototype.next = mb;
    var pb, qb, rb, ob = 256;
    if (null == qb) {
        qb = new Array,
        rb = 0;
        var sb;
        if (window.crypto && window.crypto.getRandomValues) {
            var tb = new Uint32Array(256);
            for (window.crypto.getRandomValues(tb),
            sb = 0; sb < tb.length; ++sb)
                qb[rb++] = 255 & tb[sb]
        }
        var ub = function(a) {
            if (this.count = this.count || 0,
            this.count >= 256 || rb >= ob)
                return void (window.removeEventListener ? window.removeEventListener("mousemove", ub, !1) : window.detachEvent && window.detachEvent("onmousemove", ub));
            try {
                var b = a.x + a.y;
                qb[rb++] = 255 & b,
                this.count += 1
            } catch (c) {}
        };
        window.addEventListener ? window.addEventListener("mousemove", ub, !1) : window.attachEvent && window.attachEvent("onmousemove", ub)
    }
    xb.prototype.nextBytes = wb,
    Cb.prototype.doPublic = Eb,
    Cb.prototype.setPublic = Db,
    Cb.prototype.encrypt = Fb,
    Cb.prototype.doPrivate = Kb,
    Cb.prototype.setPrivate = Hb,
    Cb.prototype.setPrivateEx = Ib,
    Cb.prototype.generate = Jb,
    Cb.prototype.decrypt = Lb,
    function() {
        var a = function(a, b, c) {
            var d = new xb
              , g = a >> 1;
            this.e = parseInt(b, 16);
            var h = new e(b,16)
              , i = this
              , j = function() {
                var b = function() {
                    if (i.p.compareTo(i.q) <= 0) {
                        var a = i.p;
                        i.p = i.q,
                        i.q = a
                    }
                    var b = i.p.subtract(e.ONE)
                      , d = i.q.subtract(e.ONE)
                      , f = b.multiply(d);
                    0 == f.gcd(h).compareTo(e.ONE) ? (i.n = i.p.multiply(i.q),
                    i.d = h.modInverse(f),
                    i.dmp1 = i.d.mod(b),
                    i.dmq1 = i.d.mod(d),
                    i.coeff = i.q.modInverse(i.p),
                    setTimeout(function() {
                        c()
                    }, 0)) : setTimeout(j, 0)
                }
                  , k = function() {
                    i.q = f(),
                    i.q.fromNumberAsync(g, 1, d, function() {
                        i.q.subtract(e.ONE).gcda(h, function(a) {
                            0 == a.compareTo(e.ONE) && i.q.isProbablePrime(10) ? setTimeout(b, 0) : setTimeout(k, 0)
                        })
                    })
                }
                  , l = function() {
                    i.p = f(),
                    i.p.fromNumberAsync(a - g, 1, d, function() {
                        i.p.subtract(e.ONE).gcda(h, function(a) {
                            0 == a.compareTo(e.ONE) && i.p.isProbablePrime(10) ? setTimeout(k, 0) : setTimeout(l, 0)
                        })
                    })
                };
                setTimeout(l, 0)
            };
            setTimeout(j, 0)
        };
        Cb.prototype.generateAsync = a;
        var b = function(a, b) {
            var c = this.s < 0 ? this.negate() : this.clone()
              , d = a.s < 0 ? a.negate() : a.clone();
            if (c.compareTo(d) < 0) {
                var e = c;
                c = d,
                d = e
            }
            var f = c.getLowestSetBit()
              , g = d.getLowestSetBit();
            if (0 > g)
                return void b(c);
            g > f && (g = f),
            g > 0 && (c.rShiftTo(g, c),
            d.rShiftTo(g, d));
            var h = function() {
                (f = c.getLowestSetBit()) > 0 && c.rShiftTo(f, c),
                (f = d.getLowestSetBit()) > 0 && d.rShiftTo(f, d),
                c.compareTo(d) >= 0 ? (c.subTo(d, c),
                c.rShiftTo(1, c)) : (d.subTo(c, d),
                d.rShiftTo(1, d)),
                c.signum() > 0 ? setTimeout(h, 0) : (g > 0 && d.lShiftTo(g, d),
                setTimeout(function() {
                    b(d)
                }, 0))
            };
            setTimeout(h, 10)
        };
        e.prototype.gcda = b;
        var c = function(a, b, c, d) {
            if ("number" == typeof b)
                if (2 > a)
                    this.fromInt(1);
                else {
                    this.fromNumber(a, c),
                    this.testBit(a - 1) || this.bitwiseTo(e.ONE.shiftLeft(a - 1), pa, this),
                    this.isEven() && this.dAddOffset(1, 0);
                    var f = this
                      , g = function() {
                        f.dAddOffset(2, 0),
                        f.bitLength() > a && f.subTo(e.ONE.shiftLeft(a - 1), f),
                        f.isProbablePrime(b) ? setTimeout(function() {
                            d()
                        }, 0) : setTimeout(g, 0)
                    };
                    setTimeout(g, 0)
                }
            else {
                var h = new Array
                  , i = 7 & a;
                h.length = (a >> 3) + 1,
                b.nextBytes(h),
                i > 0 ? h[0] &= (1 << i) - 1 : h[0] = 0,
                this.fromString(h, 256)
            }
        };
        e.prototype.fromNumberAsync = c
    }();
    var Mb = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
      , Nb = "="
      , Rb = Rb || {};
    Rb.env = Rb.env || {};
    var Sb = Rb
      , Tb = Object.prototype
      , Ub = "[object Function]"
      , Vb = ["toString", "valueOf"];
    Rb.env.parseUA = function(a) {
        var h, b = function(a) {
            var b = 0;
            return parseFloat(a.replace(/\./g, function() {
                return 1 == b++ ? "" : "."
            }))
        }, c = navigator, d = {
            ie: 0,
            opera: 0,
            gecko: 0,
            webkit: 0,
            chrome: 0,
            mobile: null,
            air: 0,
            ipad: 0,
            iphone: 0,
            ipod: 0,
            ios: null,
            android: 0,
            webos: 0,
            caja: c && c.cajaVersion,
            secure: !1,
            os: null
        }, e = a || navigator && navigator.userAgent, f = window && window.location, g = f && f.href;
        return d.secure = g && 0 === g.toLowerCase().indexOf("https"),
        e && (/windows|win32/i.test(e) ? d.os = "windows" : /macintosh/i.test(e) ? d.os = "macintosh" : /rhino/i.test(e) && (d.os = "rhino"),
        /KHTML/.test(e) && (d.webkit = 1),
        h = e.match(/AppleWebKit\/([^\s]*)/),
        h && h[1] && (d.webkit = b(h[1]),
        / Mobile\//.test(e) ? (d.mobile = "Apple",
        h = e.match(/OS ([^\s]*)/),
        h && h[1] && (h = b(h[1].replace("_", "."))),
        d.ios = h,
        d.ipad = d.ipod = d.iphone = 0,
        h = e.match(/iPad|iPod|iPhone/),
        h && h[0] && (d[h[0].toLowerCase()] = d.ios)) : (h = e.match(/NokiaN[^\/]*|Android \d\.\d|webOS\/\d\.\d/),
        h && (d.mobile = h[0]),
        /webOS/.test(e) && (d.mobile = "WebOS",
        h = e.match(/webOS\/([^\s]*);/),
        h && h[1] && (d.webos = b(h[1]))),
        / Android/.test(e) && (d.mobile = "Android",
        h = e.match(/Android ([^\s]*);/),
        h && h[1] && (d.android = b(h[1])))),
        h = e.match(/Chrome\/([^\s]*)/),
        h && h[1] ? d.chrome = b(h[1]) : (h = e.match(/AdobeAIR\/([^\s]*)/),
        h && (d.air = h[0]))),
        d.webkit || (h = e.match(/Opera[\s\/]([^\s]*)/),
        h && h[1] ? (d.opera = b(h[1]),
        h = e.match(/Version\/([^\s]*)/),
        h && h[1] && (d.opera = b(h[1])),
        h = e.match(/Opera Mini[^;]*/),
        h && (d.mobile = h[0])) : (h = e.match(/MSIE\s([^;]*)/),
        h && h[1] ? d.ie = b(h[1]) : (h = e.match(/Gecko\/([^\s]*)/),
        h && (d.gecko = 1,
        h = e.match(/rv:([^\s\)]*)/),
        h && h[1] && (d.gecko = b(h[1]))))))),
        d
    }
    ,
    Rb.env.ua = Rb.env.parseUA(),
    Rb.isFunction = function(a) {
        return "function" == typeof a || Tb.toString.apply(a) === Ub
    }
    ,
    Rb._IEEnumFix = Rb.env.ua.ie ? function(a, b) {
        var c, d, e;
        for (c = 0; c < Vb.length; c += 1)
            d = Vb[c],
            e = b[d],
            Sb.isFunction(e) && e != Tb[d] && (a[d] = e)
    }
    : function() {}
    ,
    Rb.extend = function(a, b, c) {
        if (!b || !a)
            throw new Error("extend failed, please check that all dependencies are included.");
        var e, d = function() {};
        if (d.prototype = b.prototype,
        a.prototype = new d,
        a.prototype.constructor = a,
        a.superclass = b.prototype,
        b.prototype.constructor == Tb.constructor && (b.prototype.constructor = b),
        c) {
            for (e in c)
                Sb.hasOwnProperty(c, e) && (a.prototype[e] = c[e]);
            Sb._IEEnumFix(a.prototype, c)
        }
    }
    ,
    "undefined" != typeof KJUR && KJUR || (KJUR = {}),
    "undefined" != typeof KJUR.asn1 && KJUR.asn1 || (KJUR.asn1 = {}),
    KJUR.asn1.ASN1Util = new function() {
        this.integerToByteHex = function(a) {
            var b = a.toString(16);
            return b.length % 2 == 1 && (b = "0" + b),
            b
        }
        ,
        this.bigIntToMinTwosComplementsHex = function(a) {
            var b = a.toString(16);
            if ("-" != b.substr(0, 1))
                b.length % 2 == 1 ? b = "0" + b : b.match(/^[0-7]/) || (b = "00" + b);
            else {
                var c = b.substr(1)
                  , d = c.length;
                d % 2 == 1 ? d += 1 : b.match(/^[0-7]/) || (d += 2);
                for (var f = "", g = 0; d > g; g++)
                    f += "f";
                var h = new e(f,16)
                  , i = h.xor(a).add(e.ONE);
                b = i.toString(16).replace(/^-/, "")
            }
            return b
        }
        ,
        this.getPEMStringFromHex = function(a, b) {
            var c = CryptoJS.enc.Hex.parse(a)
              , d = CryptoJS.enc.Base64.stringify(c)
              , e = d.replace(/(.{64})/g, "$1\r\n");
            return e = e.replace(/\r\n$/, ""),
            "-----BEGIN " + b + "-----\r\n" + e + "\r\n-----END " + b + "-----\r\n"
        }
    }
    ,
    KJUR.asn1.ASN1Object = function() {
        var e = "";
        this.getLengthHexFromValue = function() {
            if ("undefined" == typeof this.hV || null == this.hV)
                throw "this.hV is null or undefined.";
            if (this.hV.length % 2 == 1)
                throw "value hex must be even length: n=" + e.length + ",v=" + this.hV;
            var a = this.hV.length / 2
              , b = a.toString(16);
            if (b.length % 2 == 1 && (b = "0" + b),
            128 > a)
                return b;
            var c = b.length / 2;
            if (c > 15)
                throw "ASN.1 length too long to represent by 8x: n = " + a.toString(16);
            var d = 128 + c;
            return d.toString(16) + b
        }
        ,
        this.getEncodedHex = function() {
            return (null == this.hTLV || this.isModified) && (this.hV = this.getFreshValueHex(),
            this.hL = this.getLengthHexFromValue(),
            this.hTLV = this.hT + this.hL + this.hV,
            this.isModified = !1),
            this.hTLV
        }
        ,
        this.getValueHex = function() {
            return this.getEncodedHex(),
            this.hV
        }
        ,
        this.getFreshValueHex = function() {
            return ""
        }
    }
    ,
    KJUR.asn1.DERAbstractString = function(a) {
        KJUR.asn1.DERAbstractString.superclass.constructor.call(this);
        this.getString = function() {
            return this.s
        }
        ,
        this.setString = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.s = a,
            this.hV = stohex(this.s)
        }
        ,
        this.setStringHex = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.s = null,
            this.hV = a
        }
        ,
        this.getFreshValueHex = function() {
            return this.hV
        }
        ,
        "undefined" != typeof a && ("undefined" != typeof a.str ? this.setString(a.str) : "undefined" != typeof a.hex && this.setStringHex(a.hex))
    }
    ,
    Rb.extend(KJUR.asn1.DERAbstractString, KJUR.asn1.ASN1Object),
    KJUR.asn1.DERAbstractTime = function(a) {
        KJUR.asn1.DERAbstractTime.superclass.constructor.call(this);
        this.localDateToUTC = function(a) {
            utc = a.getTime() + 6e4 * a.getTimezoneOffset();
            var b = new Date(utc);
            return b
        }
        ,
        this.formatDate = function(a, b) {
            var c = this.zeroPadding
              , d = this.localDateToUTC(a)
              , e = String(d.getFullYear());
            "utc" == b && (e = e.substr(2, 2));
            var f = c(String(d.getMonth() + 1), 2)
              , g = c(String(d.getDate()), 2)
              , h = c(String(d.getHours()), 2)
              , i = c(String(d.getMinutes()), 2)
              , j = c(String(d.getSeconds()), 2);
            return e + f + g + h + i + j + "Z"
        }
        ,
        this.zeroPadding = function(a, b) {
            return a.length >= b ? a : new Array(b - a.length + 1).join("0") + a
        }
        ,
        this.getString = function() {
            return this.s
        }
        ,
        this.setString = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.s = a,
            this.hV = stohex(this.s)
        }
        ,
        this.setByDateValue = function(a, b, c, d, e, f) {
            var g = new Date(Date.UTC(a, b - 1, c, d, e, f, 0));
            this.setByDate(g)
        }
        ,
        this.getFreshValueHex = function() {
            return this.hV
        }
    }
    ,
    Rb.extend(KJUR.asn1.DERAbstractTime, KJUR.asn1.ASN1Object),
    KJUR.asn1.DERAbstractStructured = function(a) {
        KJUR.asn1.DERAbstractString.superclass.constructor.call(this);
        this.setByASN1ObjectArray = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.asn1Array = a
        }
        ,
        this.appendASN1Object = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.asn1Array.push(a)
        }
        ,
        this.asn1Array = new Array,
        "undefined" != typeof a && "undefined" != typeof a.array && (this.asn1Array = a.array)
    }
    ,
    Rb.extend(KJUR.asn1.DERAbstractStructured, KJUR.asn1.ASN1Object),
    KJUR.asn1.DERBoolean = function() {
        KJUR.asn1.DERBoolean.superclass.constructor.call(this),
        this.hT = "01",
        this.hTLV = "0101ff"
    }
    ,
    Rb.extend(KJUR.asn1.DERBoolean, KJUR.asn1.ASN1Object),
    KJUR.asn1.DERInteger = function(a) {
        KJUR.asn1.DERInteger.superclass.constructor.call(this),
        this.hT = "02",
        this.setByBigInteger = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.hV = KJUR.asn1.ASN1Util.bigIntToMinTwosComplementsHex(a)
        }
        ,
        this.setByInteger = function(a) {
            var b = new e(String(a),10);
            this.setByBigInteger(b)
        }
        ,
        this.setValueHex = function(a) {
            this.hV = a
        }
        ,
        this.getFreshValueHex = function() {
            return this.hV
        }
        ,
        "undefined" != typeof a && ("undefined" != typeof a.bigint ? this.setByBigInteger(a.bigint) : "undefined" != typeof a["int"] ? this.setByInteger(a["int"]) : "undefined" != typeof a.hex && this.setValueHex(a.hex))
    }
    ,
    Rb.extend(KJUR.asn1.DERInteger, KJUR.asn1.ASN1Object),
    KJUR.asn1.DERBitString = function(a) {
        KJUR.asn1.DERBitString.superclass.constructor.call(this),
        this.hT = "03",
        this.setHexValueIncludingUnusedBits = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.hV = a
        }
        ,
        this.setUnusedBitsAndHexValue = function(a, b) {
            if (0 > a || a > 7)
                throw "unused bits shall be from 0 to 7: u = " + a;
            var c = "0" + a;
            this.hTLV = null,
            this.isModified = !0,
            this.hV = c + b
        }
        ,
        this.setByBinaryString = function(a) {
            a = a.replace(/0+$/, "");
            var b = 8 - a.length % 8;
            8 == b && (b = 0);
            for (var c = 0; b >= c; c++)
                a += "0";
            for (var d = "", c = 0; c < a.length - 1; c += 8) {
                var e = a.substr(c, 8)
                  , f = parseInt(e, 2).toString(16);
                1 == f.length && (f = "0" + f),
                d += f
            }
            this.hTLV = null,
            this.isModified = !0,
            this.hV = "0" + b + d
        }
        ,
        this.setByBooleanArray = function(a) {
            for (var b = "", c = 0; c < a.length; c++)
                b += 1 == a[c] ? "1" : "0";
            this.setByBinaryString(b)
        }
        ,
        this.newFalseArray = function(a) {
            for (var b = new Array(a), c = 0; a > c; c++)
                b[c] = !1;
            return b
        }
        ,
        this.getFreshValueHex = function() {
            return this.hV
        }
        ,
        "undefined" != typeof a && ("undefined" != typeof a.hex ? this.setHexValueIncludingUnusedBits(a.hex) : "undefined" != typeof a.bin ? this.setByBinaryString(a.bin) : "undefined" != typeof a.array && this.setByBooleanArray(a.array))
    }
    ,
    Rb.extend(KJUR.asn1.DERBitString, KJUR.asn1.ASN1Object),
    KJUR.asn1.DEROctetString = function(a) {
        KJUR.asn1.DEROctetString.superclass.constructor.call(this, a),
        this.hT = "04"
    }
    ,
    Rb.extend(KJUR.asn1.DEROctetString, KJUR.asn1.DERAbstractString),
    KJUR.asn1.DERNull = function() {
        KJUR.asn1.DERNull.superclass.constructor.call(this),
        this.hT = "05",
        this.hTLV = "0500"
    }
    ,
    Rb.extend(KJUR.asn1.DERNull, KJUR.asn1.ASN1Object),
    KJUR.asn1.DERObjectIdentifier = function(a) {
        var b = function(a) {
            var b = a.toString(16);
            return 1 == b.length && (b = "0" + b),
            b
        }
          , c = function(a) {
            var c = ""
              , d = new e(a,10)
              , f = d.toString(2)
              , g = 7 - f.length % 7;
            7 == g && (g = 0);
            for (var h = "", i = 0; g > i; i++)
                h += "0";
            f = h + f;
            for (var i = 0; i < f.length - 1; i += 7) {
                var j = f.substr(i, 7);
                i != f.length - 7 && (j = "1" + j),
                c += b(parseInt(j, 2))
            }
            return c
        };
        KJUR.asn1.DERObjectIdentifier.superclass.constructor.call(this),
        this.hT = "06",
        this.setValueHex = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.s = null,
            this.hV = a
        }
        ,
        this.setValueOidString = function(a) {
            if (!a.match(/^[0-9.]+$/))
                throw "malformed oid string: " + a;
            var d = ""
              , e = a.split(".")
              , f = 40 * parseInt(e[0]) + parseInt(e[1]);
            d += b(f),
            e.splice(0, 2);
            for (var g = 0; g < e.length; g++)
                d += c(e[g]);
            this.hTLV = null,
            this.isModified = !0,
            this.s = null,
            this.hV = d
        }
        ,
        this.setValueName = function(a) {
            if ("undefined" == typeof KJUR.asn1.x509.OID.name2oidList[a])
                throw "DERObjectIdentifier oidName undefined: " + a;
            var b = KJUR.asn1.x509.OID.name2oidList[a];
            this.setValueOidString(b)
        }
        ,
        this.getFreshValueHex = function() {
            return this.hV
        }
        ,
        "undefined" != typeof a && ("undefined" != typeof a.oid ? this.setValueOidString(a.oid) : "undefined" != typeof a.hex ? this.setValueHex(a.hex) : "undefined" != typeof a.name && this.setValueName(a.name))
    }
    ,
    Rb.extend(KJUR.asn1.DERObjectIdentifier, KJUR.asn1.ASN1Object),
    KJUR.asn1.DERUTF8String = function(a) {
        KJUR.asn1.DERUTF8String.superclass.constructor.call(this, a),
        this.hT = "0c"
    }
    ,
    Rb.extend(KJUR.asn1.DERUTF8String, KJUR.asn1.DERAbstractString),
    KJUR.asn1.DERNumericString = function(a) {
        KJUR.asn1.DERNumericString.superclass.constructor.call(this, a),
        this.hT = "12"
    }
    ,
    Rb.extend(KJUR.asn1.DERNumericString, KJUR.asn1.DERAbstractString),
    KJUR.asn1.DERPrintableString = function(a) {
        KJUR.asn1.DERPrintableString.superclass.constructor.call(this, a),
        this.hT = "13"
    }
    ,
    Rb.extend(KJUR.asn1.DERPrintableString, KJUR.asn1.DERAbstractString),
    KJUR.asn1.DERTeletexString = function(a) {
        KJUR.asn1.DERTeletexString.superclass.constructor.call(this, a),
        this.hT = "14"
    }
    ,
    Rb.extend(KJUR.asn1.DERTeletexString, KJUR.asn1.DERAbstractString),
    KJUR.asn1.DERIA5String = function(a) {
        KJUR.asn1.DERIA5String.superclass.constructor.call(this, a),
        this.hT = "16"
    }
    ,
    Rb.extend(KJUR.asn1.DERIA5String, KJUR.asn1.DERAbstractString),
    KJUR.asn1.DERUTCTime = function(a) {
        KJUR.asn1.DERUTCTime.superclass.constructor.call(this, a),
        this.hT = "17",
        this.setByDate = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.date = a,
            this.s = this.formatDate(this.date, "utc"),
            this.hV = stohex(this.s)
        }
        ,
        "undefined" != typeof a && ("undefined" != typeof a.str ? this.setString(a.str) : "undefined" != typeof a.hex ? this.setStringHex(a.hex) : "undefined" != typeof a.date && this.setByDate(a.date))
    }
    ,
    Rb.extend(KJUR.asn1.DERUTCTime, KJUR.asn1.DERAbstractTime),
    KJUR.asn1.DERGeneralizedTime = function(a) {
        KJUR.asn1.DERGeneralizedTime.superclass.constructor.call(this, a),
        this.hT = "18",
        this.setByDate = function(a) {
            this.hTLV = null,
            this.isModified = !0,
            this.date = a,
            this.s = this.formatDate(this.date, "gen"),
            this.hV = stohex(this.s)
        }
        ,
        "undefined" != typeof a && ("undefined" != typeof a.str ? this.setString(a.str) : "undefined" != typeof a.hex ? this.setStringHex(a.hex) : "undefined" != typeof a.date && this.setByDate(a.date))
    }
    ,
    Rb.extend(KJUR.asn1.DERGeneralizedTime, KJUR.asn1.DERAbstractTime),
    KJUR.asn1.DERSequence = function(a) {
        KJUR.asn1.DERSequence.superclass.constructor.call(this, a),
        this.hT = "30",
        this.getFreshValueHex = function() {
            for (var a = "", b = 0; b < this.asn1Array.length; b++) {
                var c = this.asn1Array[b];
                a += c.getEncodedHex()
            }
            return this.hV = a,
            this.hV
        }
    }
    ,
    Rb.extend(KJUR.asn1.DERSequence, KJUR.asn1.DERAbstractStructured),
    KJUR.asn1.DERSet = function(a) {
        KJUR.asn1.DERSet.superclass.constructor.call(this, a),
        this.hT = "31",
        this.getFreshValueHex = function() {
            for (var a = new Array, b = 0; b < this.asn1Array.length; b++) {
                var c = this.asn1Array[b];
                a.push(c.getEncodedHex())
            }
            return a.sort(),
            this.hV = a.join(""),
            this.hV
        }
    }
    ,
    Rb.extend(KJUR.asn1.DERSet, KJUR.asn1.DERAbstractStructured),
    KJUR.asn1.DERTaggedObject = function(a) {
        KJUR.asn1.DERTaggedObject.superclass.constructor.call(this),
        this.hT = "a0",
        this.hV = "",
        this.isExplicit = !0,
        this.asn1Object = null,
        this.setASN1Object = function(a, b, c) {
            this.hT = b,
            this.isExplicit = a,
            this.asn1Object = c,
            this.isExplicit ? (this.hV = this.asn1Object.getEncodedHex(),
            this.hTLV = null,
            this.isModified = !0) : (this.hV = null,
            this.hTLV = c.getEncodedHex(),
            this.hTLV = this.hTLV.replace(/^../, b),
            this.isModified = !1)
        }
        ,
        this.getFreshValueHex = function() {
            return this.hV
        }
        ,
        "undefined" != typeof a && ("undefined" != typeof a.tag && (this.hT = a.tag),
        "undefined" != typeof a.explicit && (this.isExplicit = a.explicit),
        "undefined" != typeof a.obj && (this.asn1Object = a.obj,
        this.setASN1Object(this.isExplicit, this.hT, this.asn1Object)))
    }
    ,
    Rb.extend(KJUR.asn1.DERTaggedObject, KJUR.asn1.ASN1Object),
    function(a) {
        "use strict";
        var c, b = {};
        b.decode = function(b) {
            var d;
            if (c === a) {
                var e = "0123456789ABCDEF"
                  , f = " \f\n\r	\xa0\u2028\u2029";
                for (c = [],
                d = 0; 16 > d; ++d)
                    c[e.charAt(d)] = d;
                for (e = e.toLowerCase(),
                d = 10; 16 > d; ++d)
                    c[e.charAt(d)] = d;
                for (d = 0; d < f.length; ++d)
                    c[f.charAt(d)] = -1
            }
            var g = []
              , h = 0
              , i = 0;
            for (d = 0; d < b.length; ++d) {
                var j = b.charAt(d);
                if ("=" == j)
                    break;
                if (j = c[j],
                -1 != j) {
                    if (j === a)
                        throw "Illegal character at offset " + d;
                    h |= j,
                    ++i >= 2 ? (g[g.length] = h,
                    h = 0,
                    i = 0) : h <<= 4
                }
            }
            if (i)
                throw "Hex encoding incomplete: 4 bits missing";
            return g
        }
        ,
        window.Hex = b
    }(),
    function(a) {
        "use strict";
        var c, b = {};
        b.decode = function(b) {
            var d;
            if (c === a) {
                var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
                  , f = "= \f\n\r	\xa0\u2028\u2029";
                for (c = [],
                d = 0; 64 > d; ++d)
                    c[e.charAt(d)] = d;
                for (d = 0; d < f.length; ++d)
                    c[f.charAt(d)] = -1
            }
            var g = []
              , h = 0
              , i = 0;
            for (d = 0; d < b.length; ++d) {
                var j = b.charAt(d);
                if ("=" == j)
                    break;
                if (j = c[j],
                -1 != j) {
                    if (j === a)
                        throw "Illegal character at offset " + d;
                    h |= j,
                    ++i >= 4 ? (g[g.length] = h >> 16,
                    g[g.length] = h >> 8 & 255,
                    g[g.length] = 255 & h,
                    h = 0,
                    i = 0) : h <<= 6
                }
            }
            switch (i) {
            case 1:
                throw "Base64 encoding incomplete: at least 2 bits missing";
            case 2:
                g[g.length] = h >> 10;
                break;
            case 3:
                g[g.length] = h >> 16,
                g[g.length] = h >> 8 & 255
            }
            return g
        }
        ,
        b.re = /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/,
        b.unarmor = function(a) {
            var c = b.re.exec(a);
            if (c)
                if (c[1])
                    a = c[1];
                else {
                    if (!c[2])
                        throw "RegExp out of sync";
                    a = c[2]
                }
            return b.decode(a)
        }
        ,
        window.Base64 = b
    }(),
    function(a) {
        "use strict";
        function e(a, b) {
            a instanceof e ? (this.enc = a.enc,
            this.pos = a.pos) : (this.enc = a,
            this.pos = b)
        }
        function f(a, b, c, d, e) {
            this.stream = a,
            this.header = b,
            this.length = c,
            this.tag = d,
            this.sub = e
        }
        var b = 100
          , c = "\u2026"
          , d = {
            tag: function(a, b) {
                var c = document.createElement(a);
                return c.className = b,
                c
            },
            text: function(a) {
                return document.createTextNode(a)
            }
        };
        e.prototype.get = function(b) {
            if (b === a && (b = this.pos++),
            b >= this.enc.length)
                throw "Requesting byte offset " + b + " on a stream of length " + this.enc.length;
            return this.enc[b]
        }
        ,
        e.prototype.hexDigits = "0123456789ABCDEF",
        e.prototype.hexByte = function(a) {
            return this.hexDigits.charAt(a >> 4 & 15) + this.hexDigits.charAt(15 & a)
        }
        ,
        e.prototype.hexDump = function(a, b, c) {
            for (var d = "", e = a; b > e; ++e)
                if (d += this.hexByte(this.get(e)),
                c !== !0)
                    switch (15 & e) {
                    case 7:
                        d += "  ";
                        break;
                    case 15:
                        d += "\n";
                        break;
                    default:
                        d += " "
                    }
            return d
        }
        ,
        e.prototype.parseStringISO = function(a, b) {
            for (var c = "", d = a; b > d; ++d)
                c += String.fromCharCode(this.get(d));
            return c
        }
        ,
        e.prototype.parseStringUTF = function(a, b) {
            for (var c = "", d = a; b > d; ) {
                var e = this.get(d++);
                c += 128 > e ? String.fromCharCode(e) : e > 191 && 224 > e ? String.fromCharCode((31 & e) << 6 | 63 & this.get(d++)) : String.fromCharCode((15 & e) << 12 | (63 & this.get(d++)) << 6 | 63 & this.get(d++))
            }
            return c
        }
        ,
        e.prototype.parseStringBMP = function(a, b) {
            for (var c = "", d = a; b > d; d += 2) {
                var e = this.get(d)
                  , f = this.get(d + 1);
                c += String.fromCharCode((e << 8) + f)
            }
            return c
        }
        ,
        e.prototype.reTime = /^((?:1[89]|2\d)?\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/,
        e.prototype.parseTime = function(a, b) {
            var c = this.parseStringISO(a, b)
              , d = this.reTime.exec(c);
            return d ? (c = d[1] + "-" + d[2] + "-" + d[3] + " " + d[4],
            d[5] && (c += ":" + d[5],
            d[6] && (c += ":" + d[6],
            d[7] && (c += "." + d[7]))),
            d[8] && (c += " UTC",
            "Z" != d[8] && (c += d[8],
            d[9] && (c += ":" + d[9]))),
            c) : "Unrecognized time: " + c
        }
        ,
        e.prototype.parseInteger = function(a, b) {
            var c = b - a;
            if (c > 4) {
                c <<= 3;
                var d = this.get(a);
                if (0 === d)
                    c -= 8;
                else
                    for (; 128 > d; )
                        d <<= 1,
                        --c;
                return "(" + c + " bit)"
            }
            for (var e = 0, f = a; b > f; ++f)
                e = e << 8 | this.get(f);
            return e
        }
        ,
        e.prototype.parseBitString = function(a, b) {
            var c = this.get(a)
              , d = (b - a - 1 << 3) - c
              , e = "(" + d + " bit)";
            if (20 >= d) {
                var f = c;
                e += " ";
                for (var g = b - 1; g > a; --g) {
                    for (var h = this.get(g), i = f; 8 > i; ++i)
                        e += h >> i & 1 ? "1" : "0";
                    f = 0
                }
            }
            return e
        }
        ,
        e.prototype.parseOctetString = function(a, d) {
            var e = d - a
              , f = "(" + e + " byte) ";
            e > b && (d = a + b);
            for (var g = a; d > g; ++g)
                f += this.hexByte(this.get(g));
            return e > b && (f += c),
            f
        }
        ,
        e.prototype.parseOID = function(a, b) {
            for (var c = "", d = 0, e = 0, f = a; b > f; ++f) {
                var g = this.get(f);
                if (d = d << 7 | 127 & g,
                e += 7,
                !(128 & g)) {
                    if ("" === c) {
                        var h = 80 > d ? 40 > d ? 0 : 1 : 2;
                        c = h + "." + (d - 40 * h)
                    } else
                        c += "." + (e >= 31 ? "bigint" : d);
                    d = e = 0
                }
            }
            return c
        }
        ,
        f.prototype.typeName = function() {
            if (this.tag === a)
                return "unknown";
            var b = this.tag >> 6
              , d = (this.tag >> 5 & 1,
            31 & this.tag);
            switch (b) {
            case 0:
                switch (d) {
                case 0:
                    return "EOC";
                case 1:
                    return "BOOLEAN";
                case 2:
                    return "INTEGER";
                case 3:
                    return "BIT_STRING";
                case 4:
                    return "OCTET_STRING";
                case 5:
                    return "NULL";
                case 6:
                    return "OBJECT_IDENTIFIER";
                case 7:
                    return "ObjectDescriptor";
                case 8:
                    return "EXTERNAL";
                case 9:
                    return "REAL";
                case 10:
                    return "ENUMERATED";
                case 11:
                    return "EMBEDDED_PDV";
                case 12:
                    return "UTF8String";
                case 16:
                    return "SEQUENCE";
                case 17:
                    return "SET";
                case 18:
                    return "NumericString";
                case 19:
                    return "PrintableString";
                case 20:
                    return "TeletexString";
                case 21:
                    return "VideotexString";
                case 22:
                    return "IA5String";
                case 23:
                    return "UTCTime";
                case 24:
                    return "GeneralizedTime";
                case 25:
                    return "GraphicString";
                case 26:
                    return "VisibleString";
                case 27:
                    return "GeneralString";
                case 28:
                    return "UniversalString";
                case 30:
                    return "BMPString";
                default:
                    return "Universal_" + d.toString(16)
                }
            case 1:
                return "Application_" + d.toString(16);
            case 2:
                return "[" + d + "]";
            case 3:
                return "Private_" + d.toString(16)
            }
        }
        ,
        f.prototype.reSeemsASCII = /^[ -~]+$/,
        f.prototype.content = function() {
            if (this.tag === a)
                return null;
            var d = this.tag >> 6
              , e = 31 & this.tag
              , f = this.posContent()
              , g = Math.abs(this.length);
            if (0 !== d) {
                if (null !== this.sub)
                    return "(" + this.sub.length + " elem)";
                var h = this.stream.parseStringISO(f, f + Math.min(g, b));
                return this.reSeemsASCII.test(h) ? h.substring(0, 2 * b) + (h.length > 2 * b ? c : "") : this.stream.parseOctetString(f, f + g)
            }
            switch (e) {
            case 1:
                return 0 === this.stream.get(f) ? "false" : "true";
            case 2:
                return this.stream.parseInteger(f, f + g);
            case 3:
                return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseBitString(f, f + g);
            case 4:
                return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(f, f + g);
            case 6:
                return this.stream.parseOID(f, f + g);
            case 16:
            case 17:
                return "(" + this.sub.length + " elem)";
            case 12:
                return this.stream.parseStringUTF(f, f + g);
            case 18:
            case 19:
            case 20:
            case 21:
            case 22:
            case 26:
                return this.stream.parseStringISO(f, f + g);
            case 30:
                return this.stream.parseStringBMP(f, f + g);
            case 23:
            case 24:
                return this.stream.parseTime(f, f + g)
            }
            return null
        }
        ,
        f.prototype.toString = function() {
            return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + (null === this.sub ? "null" : this.sub.length) + "]"
        }
        ,
        f.prototype.print = function(b) {
            if (b === a && (b = ""),
            document.writeln(b + this),
            null !== this.sub) {
                b += "  ";
                for (var c = 0, d = this.sub.length; d > c; ++c)
                    this.sub[c].print(b)
            }
        }
        ,
        f.prototype.toPrettyString = function(b) {
            b === a && (b = "");
            var c = b + this.typeName() + " @" + this.stream.pos;
            if (this.length >= 0 && (c += "+"),
            c += this.length,
            32 & this.tag ? c += " (constructed)" : 3 != this.tag && 4 != this.tag || null === this.sub || (c += " (encapsulates)"),
            c += "\n",
            null !== this.sub) {
                b += "  ";
                for (var d = 0, e = this.sub.length; e > d; ++d)
                    c += this.sub[d].toPrettyString(b)
            }
            return c
        }
        ,
        f.prototype.toDOM = function() {
            var a = d.tag("div", "node");
            a.asn1 = this;
            var b = d.tag("div", "head")
              , c = this.typeName().replace(/_/g, " ");
            b.innerHTML = c;
            var e = this.content();
            if (null !== e) {
                e = String(e).replace(/</g, "&lt;");
                var f = d.tag("span", "preview");
                f.appendChild(d.text(e)),
                b.appendChild(f)
            }
            a.appendChild(b),
            this.node = a,
            this.head = b;
            var g = d.tag("div", "value");
            if (c = "Offset: " + this.stream.pos + "<br/>",
            c += "Length: " + this.header + "+",
            c += this.length >= 0 ? this.length : -this.length + " (undefined)",
            32 & this.tag ? c += "<br/>(constructed)" : 3 != this.tag && 4 != this.tag || null === this.sub || (c += "<br/>(encapsulates)"),
            null !== e && (c += "<br/>Value:<br/><b>" + e + "</b>",
            "object" == typeof oids && 6 == this.tag)) {
                var h = oids[e];
                h && (h.d && (c += "<br/>" + h.d),
                h.c && (c += "<br/>" + h.c),
                h.w && (c += "<br/>(warning!)"))
            }
            g.innerHTML = c,
            a.appendChild(g);
            var i = d.tag("div", "sub");
            if (null !== this.sub)
                for (var j = 0, k = this.sub.length; k > j; ++j)
                    i.appendChild(this.sub[j].toDOM());
            return a.appendChild(i),
            b.onclick = function() {
                a.className = "node collapsed" == a.className ? "node" : "node collapsed"
            }
            ,
            a
        }
        ,
        f.prototype.posStart = function() {
            return this.stream.pos
        }
        ,
        f.prototype.posContent = function() {
            return this.stream.pos + this.header
        }
        ,
        f.prototype.posEnd = function() {
            return this.stream.pos + this.header + Math.abs(this.length)
        }
        ,
        f.prototype.fakeHover = function(a) {
            this.node.className += " hover",
            a && (this.head.className += " hover")
        }
        ,
        f.prototype.fakeOut = function(a) {
            var b = / ?hover/;
            this.node.className = this.node.className.replace(b, ""),
            a && (this.head.className = this.head.className.replace(b, ""))
        }
        ,
        f.prototype.toHexDOM_sub = function(a, b, c, e, f) {
            if (!(e >= f)) {
                var g = d.tag("span", b);
                g.appendChild(d.text(c.hexDump(e, f))),
                a.appendChild(g)
            }
        }
        ,
        f.prototype.toHexDOM = function(b) {
            var c = d.tag("span", "hex");
            if (b === a && (b = c),
            this.head.hexNode = c,
            this.head.onmouseover = function() {
                this.hexNode.className = "hexCurrent"
            }
            ,
            this.head.onmouseout = function() {
                this.hexNode.className = "hex"
            }
            ,
            c.asn1 = this,
            c.onmouseover = function() {
                var a = !b.selected;
                a && (b.selected = this.asn1,
                this.className = "hexCurrent"),
                this.asn1.fakeHover(a)
            }
            ,
            c.onmouseout = function() {
                var a = b.selected == this.asn1;
                this.asn1.fakeOut(a),
                a && (b.selected = null,
                this.className = "hex")
            }
            ,
            this.toHexDOM_sub(c, "tag", this.stream, this.posStart(), this.posStart() + 1),
            this.toHexDOM_sub(c, this.length >= 0 ? "dlen" : "ulen", this.stream, this.posStart() + 1, this.posContent()),
            null === this.sub)
                c.appendChild(d.text(this.stream.hexDump(this.posContent(), this.posEnd())));
            else if (this.sub.length > 0) {
                var e = this.sub[0]
                  , f = this.sub[this.sub.length - 1];
                this.toHexDOM_sub(c, "intro", this.stream, this.posContent(), e.posStart());
                for (var g = 0, h = this.sub.length; h > g; ++g)
                    c.appendChild(this.sub[g].toHexDOM(b));
                this.toHexDOM_sub(c, "outro", this.stream, f.posEnd(), this.posEnd())
            }
            return c
        }
        ,
        f.prototype.toHexString = function(a) {
            return this.stream.hexDump(this.posStart(), this.posEnd(), !0)
        }
        ,
        f.decodeLength = function(a) {
            var b = a.get()
              , c = 127 & b;
            if (c == b)
                return c;
            if (c > 3)
                throw "Length over 24 bits not supported at position " + (a.pos - 1);
            if (0 === c)
                return -1;
            b = 0;
            for (var d = 0; c > d; ++d)
                b = b << 8 | a.get();
            return b
        }
        ,
        f.hasContent = function(a, b, c) {
            if (32 & a)
                return !0;
            if (3 > a || a > 4)
                return !1;
            var d = new e(c);
            3 == a && d.get();
            var g = d.get();
            if (g >> 6 & 1)
                return !1;
            try {
                var h = f.decodeLength(d);
                return d.pos - c.pos + h == b
            } catch (i) {
                return !1
            }
        }
        ,
        f.decode = function(a) {
            a instanceof e || (a = new e(a,0));
            var b = new e(a)
              , c = a.get()
              , d = f.decodeLength(a)
              , g = a.pos - b.pos
              , h = null;
            if (f.hasContent(c, d, a)) {
                var i = a.pos;
                if (3 == c && a.get(),
                h = [],
                d >= 0) {
                    for (var j = i + d; a.pos < j; )
                        h[h.length] = f.decode(a);
                    if (a.pos != j)
                        throw "Content size is not correct for container starting at offset " + i
                } else
                    try {
                        for (; ; ) {
                            var k = f.decode(a);
                            if (0 === k.tag)
                                break;
                            h[h.length] = k
                        }
                        d = i - a.pos
                    } catch (l) {
                        throw "Exception while decoding undefined length content: " + l
                    }
            } else
                a.pos += d;
            return new f(b,g,d,c,h)
        }
        ,
        f.test = function() {
            for (var a = [{
                value: [39],
                expected: 39
            }, {
                value: [129, 201],
                expected: 201
            }, {
                value: [131, 254, 220, 186],
                expected: 16702650
            }], b = 0, c = a.length; c > b; ++b) {
                var g = new e(a[b].value,0)
                  , h = f.decodeLength(g);
                h != a[b].expected && document.write("In test[" + b + "] expected " + a[b].expected + " got " + h + "\n")
            }
        }
        ,
        window.ASN1 = f
    }(),
    ASN1.prototype.getHexStringValue = function() {
        var a = this.toHexString()
          , b = 2 * this.header
          , c = 2 * this.length;
        return a.substr(b, c)
    }
    ,
    Cb.prototype.parseKey = function(a) {
        try {
            var b = 0
              , c = 0
              , d = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/
              , e = d.test(a) ? Hex.decode(a) : Base64.unarmor(a)
              , f = ASN1.decode(e);
            if (3 === f.sub.length && (f = f.sub[2].sub[0]),
            9 === f.sub.length) {
                b = f.sub[1].getHexStringValue(),
                this.n = yb(b, 16),
                c = f.sub[2].getHexStringValue(),
                this.e = parseInt(c, 16);
                var g = f.sub[3].getHexStringValue();
                this.d = yb(g, 16);
                var h = f.sub[4].getHexStringValue();
                this.p = yb(h, 16);
                var i = f.sub[5].getHexStringValue();
                this.q = yb(i, 16);
                var j = f.sub[6].getHexStringValue();
                this.dmp1 = yb(j, 16);
                var k = f.sub[7].getHexStringValue();
                this.dmq1 = yb(k, 16);
                var l = f.sub[8].getHexStringValue();
                this.coeff = yb(l, 16)
            } else {
                if (2 !== f.sub.length)
                    return !1;
                var m = f.sub[1]
                  , n = m.sub[0];
                b = n.sub[0].getHexStringValue(),
                this.n = yb(b, 16),
                c = n.sub[1].getHexStringValue(),
                this.e = parseInt(c, 16)
            }
            return !0
        } catch (o) {
            return !1
        }
    }
    ,
    Cb.prototype.getPrivateBaseKey = function() {
        var a = {
            array: [new KJUR.asn1.DERInteger({
                "int": 0
            }), new KJUR.asn1.DERInteger({
                bigint: this.n
            }), new KJUR.asn1.DERInteger({
                "int": this.e
            }), new KJUR.asn1.DERInteger({
                bigint: this.d
            }), new KJUR.asn1.DERInteger({
                bigint: this.p
            }), new KJUR.asn1.DERInteger({
                bigint: this.q
            }), new KJUR.asn1.DERInteger({
                bigint: this.dmp1
            }), new KJUR.asn1.DERInteger({
                bigint: this.dmq1
            }), new KJUR.asn1.DERInteger({
                bigint: this.coeff
            })]
        }
          , b = new KJUR.asn1.DERSequence(a);
        return b.getEncodedHex()
    }
    ,
    Cb.prototype.getPrivateBaseKeyB64 = function() {
        return Ob(this.getPrivateBaseKey())
    }
    ,
    Cb.prototype.getPublicBaseKey = function() {
        var a = {
            array: [new KJUR.asn1.DERObjectIdentifier({
                oid: "1.2.840.113549.1.1.1"
            }), new KJUR.asn1.DERNull]
        }
          , b = new KJUR.asn1.DERSequence(a);
        a = {
            array: [new KJUR.asn1.DERInteger({
                bigint: this.n
            }), new KJUR.asn1.DERInteger({
                "int": this.e
            })]
        };
        var c = new KJUR.asn1.DERSequence(a);
        a = {
            hex: "00" + c.getEncodedHex()
        };
        var d = new KJUR.asn1.DERBitString(a);
        a = {
            array: [b, d]
        };
        var e = new KJUR.asn1.DERSequence(a);
        return e.getEncodedHex()
    }
    ,
    Cb.prototype.getPublicBaseKeyB64 = function() {
        return Ob(this.getPublicBaseKey())
    }
    ,
    Cb.prototype.wordwrap = function(a, b) {
        if (b = b || 64,
        !a)
            return a;
        var c = "(.{1," + b + "})( +|$\n?)|(.{1," + b + "})";
        return a.match(RegExp(c, "g")).join("\n")
    }
    ,
    Cb.prototype.getPrivateKey = function() {
        var a = "-----BEGIN RSA PRIVATE KEY-----\n";
        return a += this.wordwrap(this.getPrivateBaseKeyB64()) + "\n",
        a += "-----END RSA PRIVATE KEY-----"
    }
    ,
    Cb.prototype.getPublicKey = function() {
        var a = "-----BEGIN PUBLIC KEY-----\n";
        return a += this.wordwrap(this.getPublicBaseKeyB64()) + "\n",
        a += "-----END PUBLIC KEY-----"
    }
    ,
    Cb.prototype.hasPublicKeyProperty = function(a) {
        return a = a || {},
        a.hasOwnProperty("n") && a.hasOwnProperty("e")
    }
    ,
    Cb.prototype.hasPrivateKeyProperty = function(a) {
        return a = a || {},
        a.hasOwnProperty("n") && a.hasOwnProperty("e") && a.hasOwnProperty("d") && a.hasOwnProperty("p") && a.hasOwnProperty("q") && a.hasOwnProperty("dmp1") && a.hasOwnProperty("dmq1") && a.hasOwnProperty("coeff")
    }
    ,
    Cb.prototype.parsePropertiesFrom = function(a) {
        this.n = a.n,
        this.e = a.e,
        a.hasOwnProperty("d") && (this.d = a.d,
        this.p = a.p,
        this.q = a.q,
        this.dmp1 = a.dmp1,
        this.dmq1 = a.dmq1,
        this.coeff = a.coeff)
    }
    ;
    var Wb = function(a) {
        Cb.call(this),
        a && ("string" == typeof a ? this.parseKey(a) : (this.hasPrivateKeyProperty(a) || this.hasPublicKeyProperty(a)) && this.parsePropertiesFrom(a))
    };
    Wb.prototype = new Cb,
    Wb.prototype.constructor = Wb;
    var Xb = function(a) {
        a = a || {},
        this.default_key_size = parseInt(a.default_key_size) || 1024,
        this.default_public_exponent = a.default_public_exponent || "010001",
        this.log = a.log || !1,
        this.key = null
    };
    Xb.prototype.setKey = function(a) {
        this.log && this.key && console.warn("A key was already set, overriding existing."),
        this.key = new Wb(a)
    }
    ,
    Xb.prototype.setPrivateKey = function(a) {
        this.setKey(a)
    }
    ,
    Xb.prototype.setPublicKey = function(a) {
        this.setKey(a)
    }
    ,
    Xb.prototype.decrypt = function(a) {
        try {
            return this.getKey().decrypt(Pb(a))
        } catch (b) {
            return !1
        }
    }
    ,
    Xb.prototype.encrypt_to_b64 = function(a) {
        try {
            return Ob(this.getKey().encrypt(a))
        } catch (b) {
            return !1
        }
    }
    ,
    Xb.prototype.encrypt = function(a) {
        try {
            return this.getKey().encrypt(a)
        } catch (b) {
            return !1
        }
    }
    ,
    Xb.prototype.getKey = function(a) {
        if (!this.key) {
            if (this.key = new Wb,
            a && "[object Function]" === {}.toString.call(a))
                return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, a);
            this.key.generate(this.default_key_size, this.default_public_exponent)
        }
        return this.key
    }
    ,
    Xb.prototype.getPrivateKey = function() {
        return this.getKey().getPrivateKey()
    }
    ,
    Xb.prototype.getPrivateKeyB64 = function() {
        return this.getKey().getPrivateBaseKeyB64()
    }
    ,
    Xb.prototype.getPublicKey = function() {
        return this.getKey().getPublicKey()
    }
    ,
    Xb.prototype.getPublicKeyB64 = function() {
        return this.getKey().getPublicBaseKeyB64()
    }
    ,
    Xb.version = "2.3.1",
    window.JSEncrypt = Xb
});


function RSAencode(str) {
    var pubk = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC/M868kojjC5nTlW2VAXwWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh/Yqtv8eTpRQq6TCMyaU8u/vj5rZsqFR7wEOEL+zDdt7Xr/n7aoOwRDMYRPdnxV5PwyDLYrVGX4/x4+SxcpbflgchjPHx10ubEd7KM2QIDAQAB';
    var result = '';
    if (pubk && str) {
        var encrypt = new JSEncrypt();
        encrypt.setPublicKey(pubk);
        result = encrypt.encrypt(encodeURI(str));
    }
    return result;
}

console.log('result',RSAencode('13672684688'));