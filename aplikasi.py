import React, { useState, useEffect } from "react";
import { base44 } from "@/api/base44Client";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { useToast } from "@/components/ui/use-toast";
import { Award, Plus, Search, Edit2, Printer } from "lucide-react";
import { Badge } from "@/components/ui/badge";

export default function Certificates() {
  const [certificates, setCertificates] = useState([]);
  const [trainings, setTrainings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [form, setForm] = useState({ training_id: "", participant_name: "", certificate_number: "", issue_date: "", training_title: "", status: "Draft" });
  const [search, setSearch] = useState("");
  const { toast } = useToast();

  const load = async () => {
    const [c, t] = await Promise.all([
      base44.entities.Certificate.list("-created_date", 50),
      base44.entities.Training.list("-created_date", 50)
    ]);
    setCertificates(c);
    setTrainings(t);
    setLoading(false);
  };

  useEffect(() => { load(); }, []);

  const handleSave = async () => {
    const training = trainings.find(t => t.id === form.training_id);
    await base44.entities.Certificate.create({ ...form, training_title: training?.title || "" });
    toast({ title: "Sertifikat ditambahkan" });
    setShowForm(false);
    setForm({ training_id: "", participant_name: "", certificate_number: "", issue_date: "", training_title: "", status: "Draft" });
    load();
  };

  const updateStatus = async (id, status) => {
    await base44.entities.Certificate.update(id, { status });
    toast({ title: `Status diubah ke ${status}` });
    load();
  };

  const statusColors = { "Draft": "bg-gray-100 text-gray-600", "Terbit": "bg-green-100 text-green-700", "Dikirim": "bg-blue-100 text-blue-700" };

  const filtered = certificates.filter(c => c.participant_name?.toLowerCase().includes(search.toLowerCase()));

  if (loading) return <div className="flex items-center justify-center h-64"><div className="w-8 h-8 border-4 border-primary/20 border-t-primary rounded-full animate-spin" /></div>;

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h1 className="text-2xl font-heading font-bold">Sertifikat Terbit</h1>
          <p className="text-muted-foreground text-sm">Kelola penerbitan sertifikat pelatihan</p>
        </div>
        <Button onClick={() => setShowForm(true)}><Plus className="w-4 h-4 mr-2" /> Terbitkan Sertifikat</Button>
      </div>

      <div className="relative max-w-md">
        <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
        <Input placeholder="Cari peserta..." value={search} onChange={e => setSearch(e.target.value)} className="pl-9" />
      </div>

      <div className="space-y-3">
        {filtered.map(c => (
          <Card key={c.id} className="border-none shadow-sm">
            <CardContent className="p-4 flex items-center gap-4 flex-wrap">
              <div className="w-10 h-10 rounded-lg bg-orange-100 flex items-center justify-center shrink-0">
                <Award className="w-5 h-5 text-orange-700" />
              </div>
              <div className="flex-1 min-w-0">
                <p className="font-semibold text-sm">{c.participant_name}</p>
                <p className="text-xs text-muted-foreground">No: {c.certificate_number} • {c.training_title}</p>
                <p className="text-[10px] text-muted-foreground">Terbit: {c.issue_date}</p>
              </div>
              <Badge className={`text-[10px] ${statusColors[c.status]}`}>{c.status}</Badge>
              <div className="flex gap-1">
                {c.status === "Draft" && <Button size="sm" variant="outline" onClick={() => updateStatus(c.id, "Terbit")} className="text-xs">Terbitkan</Button>}
                {c.status === "Terbit" && <Button size="sm" variant="outline" onClick={() => updateStatus(c.id, "Dikirim")} className="text-xs">Kirim</Button>}
              </div>
            </CardContent>
          </Card>
        ))}
        {filtered.length === 0 && (
          <div className="text-center py-12 text-muted-foreground">
            <Award className="w-12 h-12 mx-auto mb-3 opacity-30" />
            <p className="text-sm">Belum ada sertifikat</p>
          </div>
        )}
      </div>

      <Dialog open={showForm} onOpenChange={setShowForm}>
        <DialogContent>
          <DialogHeader><DialogTitle className="font-heading">Terbitkan Sertifikat</DialogTitle></DialogHeader>
          <div className="space-y-4">
            <div><Label>Pelatihan</Label>
              <Select value={form.training_id} onValueChange={v => setForm(f => ({ ...f, training_id: v }))}>
                <SelectTrigger><SelectValue placeholder="Pilih pelatihan" /></SelectTrigger>
                <SelectContent>{trainings.map(t => <SelectItem key={t.id} value={t.id}>{t.title}</SelectItem>)}</SelectContent>
              </Select>
            </div>
            <div><Label>Nama Peserta</Label><Input value={form.participant_name} onChange={e => setForm(f => ({ ...f, participant_name: e.target.value }))} /></div>
            <div><Label>Nomor Sertifikat</Label><Input value={form.certificate_number} onChange={e => setForm(f => ({ ...f, certificate_number: e.target.value }))} /></div>
            <div><Label>Tanggal Terbit</Label><Input type="date" value={form.issue_date} onChange={e => setForm(f => ({ ...f, issue_date: e.target.value }))} /></div>
            <Button onClick={handleSave} className="w-full">Terbitkan</Button>
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
